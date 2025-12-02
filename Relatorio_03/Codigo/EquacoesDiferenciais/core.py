import os
import sys
import time
from . import metodos
from . import relatorios
from . import graficos

class CalculadorEDO:
    
    def __init__(self, filename, tipo_problema="PVI"):
        """
        tipo_problema: "PVI" (Valor Inicial) ou "PVC" (Valor de Contorno)
        """
        self.problemas = []
        self.tipo_problema = tipo_problema
        
        input_path = os.path.join('input', filename)
        
        try:
            with open(input_path, 'r', encoding='utf-8') as file:
                for line in file:
                    if not line.strip():
                        continue
                    
                    parts = line.strip().split(";")
                    
                    # Leitura comum para todos
                    func_str = parts[0].strip()
                    y0 = float(parts[1].strip())
                    interval = [float(val) for val in parts[2].strip().split(",")]
                    
                    if tipo_problema == "PVI":
                        # Formato: func; y0; intervalo; h
                        h = float(parts[3].strip())
                        self.problemas.append({
                            'func': func_str, 'y0': y0, 'interval': interval, 'h': h
                        })
                        
                    elif tipo_problema == "PVC":
                        # Formato: func; y0; intervalo; target; h; n; [params...]
                        target = float(parts[3].strip())
                        h = float(parts[4].strip())
                        n = int(parts[5].strip())
                        
                        params = {}
                        if len(parts) > 6:
                            for p in parts[6:]:
                                key, val = p.strip().split("=")
                                params[key.strip()] = float(val.strip())
                                
                        self.problemas.append({
                            'func': func_str, 'y0': y0, 'interval': interval, 
                            'target': target, 'h': h, 'n': n, 'params': params
                        })

        except Exception as e:
            print(f"\nErro ao ler o arquivo '{input_path}': {e}")
            sys.exit()

    def _executar_metodo(self, nome_metodo, funcao_metodo, output_file):
        """Helper genérico para rodar e cronometrar."""
        start_time = time.time()
        results = []
        
        print(f"Executando {nome_metodo}...")
        
        for p in self.problemas:
            if self.tipo_problema == "PVI":
                x, y = funcao_metodo(p['func'], p['y0'], p['interval'], p['h'])
            else: # PVC
                x, y = funcao_metodo(p['func'], p['y0'], p['interval'], 
                                     p['target'], p['h'], p['n'], p['params'])
            results.append((x, y))
            
        tempo = time.time() - start_time
        path_out = os.path.join("output", output_file)
        
        relatorios.gerar_relatorio_edo(path_out, nome_metodo, results, tempo)
        print(f"Sucesso! Salvo em '{path_out}'.")

    # --- Gerar gráfico comparativo de tempos ---
    def run_comparativo(self):
        """
        Executa todos os métodos disponíveis, coleta tempos e gera:
        1. Gráfico de barras de tempo.
        2. Gráfico de linhas com as soluções (trajetórias) para cada problema.
        """
        import time
        
        # Definir quais métodos rodar baseado no tipo
        if self.tipo_problema == "PVI":
            lista_metodos = {
                "Euler Simples": metodos.euler_simples,
                "Heun": metodos.heun,
                "Euler Modificado": metodos.euler_modificado,
                "Ralston": metodos.ralston,
                "RK3": metodos.runge_kutta_3,
                "RK4": metodos.runge_kutta_4
            }
        else:
            lista_metodos = {
                "Shooting": metodos.shooting_method,
                "Dif. Finitas": metodos.diferencas_finitas
            }

        nomes = []
        tempos = []
        
        # Estrutura para armazenar as soluções de cada problema
        # { indice_problema: { "NomeMetodo": ([x...], [y...]) } }
        solucoes_por_problema = {i: {} for i in range(len(self.problemas))}

        print(f"\n--- Iniciando Comparativo de Desempenho ({self.tipo_problema}) ---")
        print(f"Processando {len(self.problemas)} problema(s) com {len(lista_metodos)} métodos...\n")

        # Loop para rodar cada método
        for nome_metodo, funcao in lista_metodos.items():
            start = time.time()
            
            # Executa para cada problema na lista
            for i, p in enumerate(self.problemas):
                if self.tipo_problema == "PVI":
                    x_res, y_res = funcao(p['func'], p['y0'], p['interval'], p['h'])
                else: # PVC
                    x_res, y_res = funcao(p['func'], p['y0'], p['interval'], 
                                          p['target'], p['h'], p['n'], p['params'])
                
                # Salva os dados para o gráfico de linhas
                solucoes_por_problema[i][nome_metodo] = (x_res, y_res)
            
            end = time.time()
            tempo_total = end - start
            
            nomes.append(nome_metodo)
            tempos.append(tempo_total)
            print(f"> {nome_metodo}: {tempo_total:.6f} s")

        # 1. Gerar Gráfico de Barras (Tempo)
        nome_arquivo_tempo = f"comparativo_{self.tipo_problema.lower()}.png"
        graficos.gerar_grafico_comparativo(nomes, tempos, nome_arquivo_tempo)
        
        # 2. Gerar Gráficos de Linha (Soluções)
        print("\nGerando gráficos das soluções...")
        for i, dados_metodos in solucoes_por_problema.items():
            graficos.gerar_grafico_solucoes(dados_metodos, id_problema=i)
            
        print("\nComparativos finalizados com sucesso!")

    def run_all_methods(self):
        """
        Executa todos os métodos disponíveis para o tipo configurado (PVI ou PVC)
        e gera os arquivos de saída individuais para cada um.
        """
        print(f"\n--- Executando TODOS os métodos para {self.tipo_problema} ---")
        
        if self.tipo_problema == "PVI":
            # Lista de (Nome do Método, Função Wrapper)
            metodos_pvi = [
                ("Método de Euler", self.run_euler),
                ("Método de Heun", self.run_heun),
                ("Euler Modificado", self.run_euler_modificado),
                ("Método de Ralston", self.run_ralston),
                ("Runge-Kutta 3ª Ordem", self.run_rk3),
                ("Runge-Kutta 4ª Ordem", self.run_rk4)
            ]
            
            for nome, funcao in metodos_pvi:
                print(f"> Rodando {nome}...")
                funcao() # Chama o wrapper que já gera o arquivo .txt
                
        elif self.tipo_problema == "PVC":
            metodos_pvc = [
                ("Shooting Method", self.run_shooting),
                ("Diferenças Finitas", self.run_finite_differences)
            ]
            
            for nome, funcao in metodos_pvc:
                print(f"> Rodando {nome}...")
                funcao()

        print(f"\n--- Todos os relatórios foram gerados na pasta 'output' ---")

    # --- Wrappers para PVI ---
    def run_euler(self):
        self._executar_metodo("Método de Euler", metodos.euler_simples, "euler_saida.txt")

    def run_heun(self):
        self._executar_metodo("Método de Heun", metodos.heun, "heun_saida.txt")
        
    def run_euler_modificado(self):
        self._executar_metodo("Euler Modificado", metodos.euler_modificado, "euler_mod_saida.txt")
        
    def run_ralston(self):
        self._executar_metodo("Método de Ralston", metodos.ralston, "ralston_saida.txt")

    def run_rk3(self):
        self._executar_metodo("Runge-Kutta 3ª Ordem", metodos.runge_kutta_3, "rk3_saida.txt")

    def run_rk4(self):
        self._executar_metodo("Runge-Kutta 4ª Ordem", metodos.runge_kutta_4, "rk4_saida.txt")

    # --- Wrappers para PVC ---
    def run_shooting(self):
        self._executar_metodo("Shooting Method", metodos.shooting_method, "shooting_saida.txt")

    def run_finite_differences(self):
        self._executar_metodo("Diferenças Finitas", metodos.diferencas_finitas, "dif_finitas_saida.txt")