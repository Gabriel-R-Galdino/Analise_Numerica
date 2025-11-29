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
        Executa todos os métodos disponíveis para o tipo de problema (PVI ou PVC),
        coleta os tempos e gera um gráfico.
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

        print(f"\n--- Iniciando Comparativo de Desempenho ({self.tipo_problema}) ---")
        print(f"Processando {len(self.problemas)} problema(s) com {len(lista_metodos)} métodos diferentes...\n")

        # Loop para rodar cada método e cronometrar
        for nome, funcao in lista_metodos.items():
            start = time.time()
            
            # Executa a função matemática pura para todos os problemas carregados
            # (Não geramos relatório de texto aqui, focamos apenas no cálculo)
            for p in self.problemas:
                if self.tipo_problema == "PVI":
                    funcao(p['func'], p['y0'], p['interval'], p['h'])
                else: # PVC
                    funcao(p['func'], p['y0'], p['interval'], 
                           p['target'], p['h'], p['n'], p['params'])
            
            end = time.time()
            tempo_total = end - start
            
            nomes.append(nome)
            tempos.append(tempo_total)
            print(f"> {nome}: {tempo_total:.6f} s")

        # Chamar o módulo de gráficos
        nome_arquivo = f"comparativo_{self.tipo_problema.lower()}.png"
        graficos.gerar_grafico_comparativo(nomes, tempos, nome_arquivo)

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