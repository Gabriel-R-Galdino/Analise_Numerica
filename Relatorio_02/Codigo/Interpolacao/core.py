import os
import sys
import time
from . import metodos
from . import relatorios

class CalculadorInterpolacao:
    
    def __init__(self, filename):
        self.data_sets = []
        try:
            input_path = os.path.join('input', filename)
            with open(input_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            for line in lines:
                if not line.strip():
                    continue
                x_values_str, y_values_str = line.strip().split(";")
                x_values = list(map(float, x_values_str.split(",")))
                y_values = list(map(float, y_values_str.split(",")))
                self.data_sets.append((x_values, y_values))

        except Exception as e:
            print(f"\nErro ao ler o arquivo '{input_path}': {e}")
            sys.exit()

    def run_lagrange(self):
        output_filename = os.path.join("output", "interpolacao_lagrange_saida.txt")
        start_time = time.time()
        
        results = []
        for (x_vals, y_vals) in self.data_sets:
            poly_expr = metodos.lagrange_polynomial(x_vals, y_vals)
            results.append(poly_expr)
            
        tempo = time.time() - start_time
        
        relatorios.gerar_relatorio_interpolacao(
            output_filename, 
            "Interpolação por Polinômios de Lagrange", 
            results, 
            tempo
        )
        print(f"\nSucesso! Relatório salvo em '{output_filename}'.")

    def run_newton(self):
        output_filename = os.path.join("output", "interpolacao_newton_saida.txt")
        start_time = time.time()
        
        results = []
        for (x_vals, y_vals) in self.data_sets:
            poly_expr = metodos.newton_divided_differences(x_vals, y_vals)
            results.append(poly_expr)
            
        tempo = time.time() - start_time
        
        relatorios.gerar_relatorio_interpolacao(
            output_filename, 
            "Interpolação por Diferenças Divididas de Newton", 
            results, 
            tempo
        )
        print(f"\nSucesso! Relatório salvo em '{output_filename}'.")