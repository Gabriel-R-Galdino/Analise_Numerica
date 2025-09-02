import os
import sys
import time
from sympy import symbols, sympify, lambdify, diff

from . import metodos
from . import relatorios

class CalculadoraNumerica:
    def __init__(self, filename):
        try:
            # A lógica de ler o arquivo e preparar a função continua aqui.
            input_path = os.path.join('input', filename)
            with open(input_path, 'r', encoding='utf-8') as f:
                self.func_str = f.readline().strip()
                self.a = float(f.readline().strip())
                self.b = float(f.readline().strip())
                tolerancia_str = f.readline().strip()
                self.tolerance = float(tolerancia_str) if tolerancia_str else 1e-8
            
            x = symbols('x')
            sym_func = sympify(self.func_str.replace('^', '**'))
            sym_deriv = diff(sym_func, x)
            
            self.f = lambdify(x, sym_func, 'numpy')
            self.f_prime = lambdify(x, sym_deriv, 'numpy')

        except FileNotFoundError:
            print(f"\nERRO: O arquivo '{input_path}' não foi encontrado.")
            sys.exit()
        except Exception as e:
            print(f"\nOcorreu um erro ao processar o arquivo de entrada: {e}")
            sys.exit()

    def run_bissecao(self):
        output_filename = os.path.join("output", "bissecao_saida.txt")
        start_time = time.time()
        
        # Chama a função do módulo de métodos
        passos, resumo = metodos.bissecao(self.f, self.a, self.b, self.tolerance)
        tempo = time.time() - start_time

        if passos is None:
            print("\nAVISO: Não há garantia de raiz no intervalo para o método da Bissecção.")
            return

        # Chama a função do módulo de relatórios
        relatorios.gerar_relatorio_bissecao(output_filename, self.func_str, passos, resumo, tempo)
        
        if resumo:
            print(f"\nSucesso! Relatório salvo em '{output_filename}'.")
        else:
            print("\nO método não convergiu no número máximo de iterações.")

    def run_falsa_posicao(self):
        output_filename = os.path.join("output", "posicao_falsa_saida.txt")
        start_time = time.time()
        
        passos, resumo = metodos.falsa_posicao(self.f, self.a, self.b, self.tolerance)
        tempo = time.time() - start_time

        if passos is None:
            print("\nAVISO: Não há garantia de raiz no intervalo para o método da Posição Falsa.")
            return

        relatorios.gerar_relatorio_falsa_posicao(output_filename, self.func_str, passos, resumo, tempo)

        if resumo:
            print(f"\nSucesso! Relatório salvo em '{output_filename}'.")
        else:
            print("\nO método não convergiu no número máximo de iterações.")
            
    def run_newton_raphson(self):
        output_filename = os.path.join("output", "newton_raphson_saida.txt")
        x0 = (self.a + self.b) / 2
        start_time = time.time()

        passos, resumo = metodos.newton_raphson(self.f, self.f_prime, x0, self.tolerance)
        tempo = time.time() - start_time
        
        relatorios.gerar_relatorio_newton(output_filename, self.func_str, x0, passos, resumo, tempo)

        if resumo and 'erro_msg' in resumo:
             print(f"\nERRO: {resumo['erro_msg']} O método falhou.")
        elif resumo:
            print(f"\nSucesso! Relatório salvo em '{output_filename}'.")
        else:
            print("\nO método não convergiu no número máximo de iterações.")

    def run_secante(self):
        output_filename = os.path.join("output", "secante_saida.txt")
        start_time = time.time()

        passos, resumo = metodos.secante(self.f, self.a, self.b, self.tolerance)
        tempo = time.time() - start_time
        
        relatorios.gerar_relatorio_secante(output_filename, self.func_str, self.a, self.b, passos, resumo, tempo)

        if resumo and 'erro_msg' in resumo:
             print(f"\nERRO: {resumo['erro_msg']} O método falhou.")
        elif resumo:
            print(f"\nSucesso! Relatório salvo em '{output_filename}'.")
        else:
            print("\nO método não convergiu no número máximo de iterações.")