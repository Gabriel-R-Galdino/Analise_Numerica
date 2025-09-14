import os
import sys
import time
import numpy as np
import ast

from . import metodos
from . import relatorios

class CalculadorDeSistemas:

    def _parse_format_lists(self, lines):
        """
        Processa formatos com listas.
        Aceita tanto '[[1,2],[3,4]]' (aninhado)
        quanto '[1,2],[3,4]' (sequência de listas).
        """
        if len(lines) < 2:
            raise ValueError("O formato de lista requer 2 linhas (matriz A e vetor b).")
        
        A_str = lines[0].strip()
        
        # Se a string da matriz A NÃO começa com '[[', significa que é o formato
        # '[r1],[r2],...' e precisa ser envolvida por colchetes para se tornar
        # uma lista de listas válida em Python.
        if not A_str.startswith('[['):
            A_str = f"[{A_str}]"

        try:
            # ast.literal_eval converte a string de uma lista/matriz para o objeto Python correspondente
            matrix_A = ast.literal_eval(A_str)
            vector_b = ast.literal_eval(lines[1].strip())
            return np.array(matrix_A, dtype=float), np.array(vector_b, dtype=float)
        except (ValueError, SyntaxError):
            raise ValueError("Erro de sintaxe ao ler o formato de lista. Verifique os colchetes e vírgulas.")

    def _parse_format_augmented(self, lines):
        """Processa o formato com dimensão + matriz aumentada (ex: 3 \n 1 2 3 4)"""
        try:
            n = int(lines[0].strip())
        except ValueError:
            raise ValueError("A primeira linha do formato de matriz aumentada deve ser um único número inteiro (a dimensão).")

        if len(lines) < n + 1:
            raise ValueError(f"Esperava {n+1} linhas, mas o arquivo contém apenas {len(lines)}.")

        matrix_A = []
        vector_b = []

        for i in range(1, n + 1):
            line_values = lines[i].strip().split()
            if len(line_values) != n + 1:
                raise ValueError(f"A linha {i+1} não contém os {n+1} elementos esperados.")
            
            row = [float(val) for val in line_values]
            matrix_A.append(row[:-1])
            vector_b.append(row[-1])
        
        return np.array(matrix_A), np.array(vector_b)

    def __init__(self, filename):
        try:
            input_path = os.path.join('input', filename)
            with open(input_path, 'r', encoding='utf-8') as f:
                lines = [line for line in f if line.strip()] # Lê todas as linhas não vazias
            
            if not lines:
                raise ValueError("O arquivo de entrada está vazio.")

            first_line = lines[0].strip()

            # LÓGICA DE DETECÇÃO DO FORMATO 
            if first_line.startswith('['):
                self.A, self.b = self._parse_format_lists(lines)
            elif first_line.isdigit():
                self.A, self.b = self._parse_format_augmented(lines)
            else:
                raise ValueError("Formato de arquivo não reconhecido. A primeira linha deve ser a dimensão (ex: '3') ou uma matriz (ex: '[...]' ou '[[...]]').")

            # Validação final das matrizes
            if self.A.shape[0] != self.A.shape[1] or self.A.shape[0] != len(self.b):
                raise ValueError("A matriz A deve ser quadrada e compatível com o vetor b.")

        except FileNotFoundError:
            print(f"\nERRO: O arquivo '{input_path}' não foi encontrado.")
            sys.exit()
        except (ValueError, IndexError) as e:
            print(f"\nOcorreu um erro de formato ao processar o arquivo de entrada: {e}")
            sys.exit()
        except Exception as e:
            print(f"\nOcorreu um erro inesperado ao processar o arquivo de entrada: {e}")
            sys.exit()
            
    def run_gauss(self):
        output_filename = os.path.join("output", "gauss_saida.txt")
        start_time = time.time()
        resumo = metodos.eliminacao_gauss(self.A, self.b)
        tempo = time.time() - start_time
        relatorios.gerar_relatorio_gauss(output_filename, self.A, self.b, resumo, tempo)
        if resumo and 'solucao' in resumo:
            print(f"\nSucesso! Relatório salvo em '{output_filename}'.")
        else:
            print(f"\nERRO: {resumo.get('erro_msg', 'Método falhou.')}")

    def run_lu(self):
        output_filename = os.path.join("output", "lu_saida.txt")
        start_time = time.time()
        resumo = metodos.fatoracao_lu(self.A, self.b)
        tempo = time.time() - start_time
        relatorios.gerar_relatorio_lu(output_filename, self.A, self.b, resumo, tempo)
        if resumo and 'solucao' in resumo:
            print(f"\nSucesso! Relatório salvo em '{output_filename}'.")
        else:
            print(f"\nERRO: {resumo.get('erro_msg', 'Método falhou.')}")

    def run_jacobi(self):
        output_filename = os.path.join("output", "jacobi_saida.txt")
        start_time = time.time()
        passos, resumo = metodos.jacobi(self.A, self.b)
        tempo = time.time() - start_time
        relatorios.gerar_relatorio_jacobi(output_filename, self.A, self.b, passos, resumo, tempo)
        if resumo:
            print(f"\nSucesso! Relatório salvo em '{output_filename}'.")
        else:
            print("\nO método não convergiu no número máximo de iterações.")

    def run_gauss_seidel(self):
        output_filename = os.path.join("output", "gauss_seidel_saida.txt")
        start_time = time.time()
        passos, resumo = metodos.gauss_seidel(self.A, self.b)
        tempo = time.time() - start_time
        relatorios.gerar_relatorio_gauss_seidel(output_filename, self.A, self.b, passos, resumo, tempo)
        if resumo:
            print(f"\nSucesso! Relatório salvo em '{output_filename}'.")
        else:
            print("\nO método não convergiu no número máximo de iterações.")