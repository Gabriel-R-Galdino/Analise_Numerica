import os
import sys
import time
import numpy as np
import ast

from . import metodos
from . import relatorios

class CalculadorDeCondicao:
    def _parse_matrix(self, lines):
        """
        Detecta e processa todos os formatos suportados.
        """
        # Formato 1: Dimensão na primeira linha
        if lines[0].isdigit() and len(lines) == int(lines[0]) + 1:
            n = int(lines[0])
            matrix_A = []
            for i in range(1, n + 1):
                row = [float(val) for val in lines[i].strip().split()]
                if len(row) != n:
                    raise ValueError(f"A linha {i+1} não contém os {n} elementos esperados.")
                matrix_A.append(row)
            return np.array(matrix_A)

        # Formatos 2 e 3: Matriz inteira em uma única linha
        if len(lines) == 1:
            line = lines[0].strip()
            if not line.startswith('[['):
                line = f"[{line}]"
            try:
                return np.array(ast.literal_eval(line), dtype=float)
            except (ValueError, SyntaxError):
                 raise ValueError("Erro de sintaxe ao ler o formato de lista de linha única.")

        # Formatos 4 e 5: Uma linha da matriz por linha do arquivo
        matrix_A = []
        num_cols = -1
        for i, line_str in enumerate(lines):
            line_str = line_str.strip()
            row = []
            try:
                if line_str.startswith('['):
                    row = ast.literal_eval(line_str)
                else:
                    row = [float(val) for val in line_str.split()]
                
                if i == 0:
                    num_cols = len(row)
                elif len(row) != num_cols:
                    raise ValueError(f"Inconsistência no número de colunas. A linha {i+1} tem {len(row)} elementos, esperado {num_cols}.")
                
                matrix_A.append(row)

            except (ValueError, SyntaxError):
                raise ValueError(f"Erro de sintaxe ao processar a linha {i+1}: '{line_str}'")
        
        return np.array(matrix_A, dtype=float)

    def __init__(self, filename):
        try:
            input_path = os.path.join('input', filename)
            with open(input_path, 'r', encoding='utf-8') as f:
                lines = [line for line in f if line.strip()]
            
            if not lines:
                raise ValueError("O arquivo de entrada está vazio.")

            self.A = self._parse_matrix(lines)

            if self.A.shape[0] != self.A.shape[1]:
                raise ValueError("A matriz de entrada deve ser quadrada.")

        except FileNotFoundError:
            print(f"\nERRO: O arquivo '{input_path}' não foi encontrado.")
            sys.exit()
        except (ValueError, IndexError) as e:
            print(f"\nOcorreu um erro de formato ao processar o arquivo de entrada: {e}")
            sys.exit()
        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e}")
            sys.exit()

    def run_condicionamento(self):
        output_filename = os.path.join("output", "condicionamento_saida.txt")
        start_time = time.time()
        resumo = metodos.numero_condicao(self.A)
        tempo = time.time() - start_time
        relatorios.gerar_relatorio_condicao(output_filename, self.A, resumo, tempo)
        if 'erro_msg' in resumo:
            print(f"\nERRO: {resumo['erro_msg']}")
        else:
            print(f"\nSucesso! Relatório salvo em '{output_filename}'.")