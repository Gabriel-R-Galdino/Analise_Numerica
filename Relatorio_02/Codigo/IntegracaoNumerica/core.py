import os
import sys
import time
from . import metodos
from . import relatorios

class CalculadorIntegracao:
    
    def __init__(self, filename):
        self.functions = []
        self.intervals = []
        self.subdivisions = []
        try:
            input_path = os.path.join('input', filename)
            with open(input_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            for line in lines:
                if not line.strip():
                    continue
                func_str, interval_str, sub_str = line.strip().split(";")
                
                self.functions.append(func_str.strip())
                self.intervals.append(list(map(float, interval_str.split(","))))
                self.subdivisions.append(int(sub_str))

        except Exception as e:
            print(f"\nErro ao ler o arquivo '{input_path}': {e}")
            sys.exit()

    def _run_method(self, method_func, output_suffix, report_title):
        """Função auxiliar genérica para rodar um método de integração."""
        output_filename = os.path.join("output", f"integracao_{output_suffix}.txt")
        start_time = time.time()
        
        results = []
        try:
            for func_str, interval, n in zip(self.functions, self.intervals, self.subdivisions):
                # O método é passado como argumento
                integral = method_func(func_str, interval[0], interval[1], n)
                results.append(integral)
                
            tempo = time.time() - start_time
            
            relatorios.gerar_relatorio_integracao(
                output_filename, 
                report_title, 
                results, 
                tempo
            )
            print(f"\nSucesso! Relatório salvo em '{output_filename}'.")
        except Exception as e:
            print(f"\nErro ao calcular o método '{report_title}': {e}")

    # --- Métodos de Integração ---
    
    def run_trapezoidal_simples(self):
        # A lógica original do "simple_trapezoidal" usava 'n' subdivisões,
        # então mantemos isso. Para um trapézio simples "real", forçaríamos n=1.
        self._run_method(
            metodos.trapezoidal, 
            "trapezio_simples", 
            "Regra do Trapézio Simples"
        )

    def run_trapezoidal_multiplos(self):
        self._run_method(
            metodos.trapezoidal, 
            "trapezio_multiplo", 
            "Regra dos Trapézios Múltiplos"
        )

    def run_simpson_1_3_simples(self):
        self._run_method(
            metodos.simpson_1_3_simple, 
            "simpson_1_3_simples", 
            "Regra de Simpson 1/3 Simples"
        )

    def run_simpson_1_3_multiplos(self):
        self._run_method(
            metodos.simpson_1_3_multiple, 
            "simpson_1_3_multiplo", 
            "Regra de Simpson 1/3 Múltipla"
        )

    def run_simpson_3_8_simples(self):
        self._run_method(
            metodos.simpson_3_8_simple, 
            "simpson_3_8_simples", 
            "Regra de Simpson 3/8 Simples"
        )

    def run_simpson_3_8_multiplos(self):
        self._run_method(
            metodos.simpson_3_8_multiple, 
            "simpson_3_8_multiplo", 
            "Regra de Simpson 3/8 Múltipla"
        )

    def run_richards(self):
        # Richards não usa 'n' da entrada, usa seus próprios valores
        self._run_method(
            metodos.richards_extrapolation, 
            "richards", 
            "Extrapolação de Richards"
        )

    def run_gaussian_quadrature(self):
        self._run_method(
            metodos.gaussian_quadrature, 
            "gauss", 
            "Quadratura de Gauss"
        )