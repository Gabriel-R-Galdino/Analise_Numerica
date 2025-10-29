import os
import sys
import time
from . import metodos
from . import relatorios

class CalculadorDerivacao:
    
    def __init__(self, filename):
        self.functions = []
        self.x_values = []
        try:
            input_path = os.path.join('input', filename)
            with open(input_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            for line in lines:
                if not line.strip():
                    continue
                func_str, x_str = line.strip().split(";")
                self.functions.append(func_str.strip())
                self.x_values.append(float(x_str.strip()))

        except Exception as e:
            print(f"\nErro ao ler o arquivo '{input_path}': {e}")
            sys.exit()

    def run_first_order(self):
        output_filename = os.path.join("output", "derivacao_primeira_ordem_saida.txt")
        start_time = time.time()
        
        results = []
        for func_str, x_val in zip(self.functions, self.x_values):
            derivada = metodos.finite_difference_first_order(func_str, x_val)
            results.append(derivada)
            
        tempo = time.time() - start_time
        
        relatorios.gerar_relatorio_derivacao(
            output_filename, 
            "Derivação Numérica de Primeira Ordem", 
            self.functions,
            results, 
            tempo
        )
        print(f"\nSucesso! Relatório salvo em '{output_filename}'.")

    def run_second_order(self):
        output_filename = os.path.join("output", "derivacao_segunda_ordem_saida.txt")
        start_time = time.time()
        
        results = []
        for func_str, x_val in zip(self.functions, self.x_values):
            derivada = metodos.finite_difference_second_order(func_str, x_val)
            results.append(derivada)
            
        tempo = time.time() - start_time
        
        relatorios.gerar_relatorio_derivacao(
            output_filename, 
            "Derivação Numérica de Segunda Ordem", 
            self.functions,
            results, 
            tempo
        )
        print(f"\nSucesso! Relatório salvo em '{output_filename}'.")