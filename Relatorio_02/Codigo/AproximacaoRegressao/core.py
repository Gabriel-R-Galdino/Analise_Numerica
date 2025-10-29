import os
import sys
import time
import math
from sympy import Symbol, sympify, integrate, zeros, E

from . import metodos
from . import relatorios

class CalculadorAproximacao:
    
    def __init__(self, filename, method_type):
        """
        Lê o arquivo de entrada.
        method_type = "discreto" para (x,y)
        method_type = "continuo" para (f(x), intervalo)
        """
        self.data_sets = []
        self.functions = []
        self.intervals = []
        
        try:
            input_path = os.path.join('input', filename)
            with open(input_path, 'r', encoding='utf-8') as file:
                for line in file:
                    if not line.strip():
                        continue
                    
                    aux = line.split(";")
                    
                    if method_type == "discreto":
                        x_vals = [eval(x_val) for x_val in aux[0].split(",")]
                        y_vals = [eval(y_val) for y_val in aux[1].strip().split(",")]
                        self.data_sets.append((x_vals, y_vals))
                    
                    elif method_type == "continuo":
                        # Mantém a função como string, será processada no 'metodos.py'
                        self.functions.append(aux[0].strip())
                        interval = [eval(x_val) for x_val in aux[1].split(",")]
                        self.intervals.append(interval)

        except Exception as e:
            print(f"\nErro ao ler o arquivo '{input_path}': {e}")
            sys.exit()

    def run_linear_regression(self):
        output_filename = os.path.join("output", "regressao_linear_saida.txt")
        start_time = time.time()
        
        results = []
        for (x_vals, y_vals) in self.data_sets:
            # Chama a função do módulo de métodos
            a, b = metodos.linear_regression(x_vals, y_vals)
            results.append({'a': a, 'b': b})
            
        tempo = time.time() - start_time
        
        # Chama a função do módulo de relatórios
        relatorios.gerar_relatorio_regressao_linear(output_filename, results, tempo)
        print(f"\nSucesso! Relatório salvo em '{output_filename}'.")

    def run_discrete_polynomial(self):
        output_filename = os.path.join("output", "aprox_polinomial_discreta_saida.txt")
        start_time = time.time()

        results = []
        for (x_vals, y_vals) in self.data_sets:
            # Chama a função do módulo de métodos
            poly_expr = metodos.discrete_polynomial_approximation(x_vals, y_vals)
            results.append(poly_expr)

        tempo = time.time() - start_time
        
        # Chama a função do módulo de relatórios
        relatorios.gerar_relatorio_aprox_polinomial(
            output_filename, 
            "Aproximação Polinomial Discreta", 
            results, 
            tempo
        )
        print(f"\nSucesso! Relatório salvo em '{output_filename}'.")

    def run_continuous_polynomial(self):
        output_filename = os.path.join("output", "aprox_polinomial_continua_saida.txt")
        start_time = time.time()

        results = []
        for func_str, interval in zip(self.functions, self.intervals):
            # Chama a função do módulo de métodos
            poly_expr = metodos.continuous_polynomial_approximation(func_str, interval)
            results.append(poly_expr)

        tempo = time.time() - start_time
        
        # Chama a função do módulo de relatórios
        relatorios.gerar_relatorio_aprox_polinomial(
            output_filename, 
            "Aproximação Polinomial Contínua", 
            results, 
            tempo
        )
        print(f"\nSucesso! Relatório salvo em '{output_filename}'.")