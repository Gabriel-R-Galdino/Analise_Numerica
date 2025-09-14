"""
Módulo para geração de relatórios de saída.
"""
import numpy as np

def _escrever_resumo_iterativo(file, resumo, tempo):
    """Escreve o bloco de resumo final para métodos iterativos."""
    file.write("\n" + "-"*75 + "\n")
    file.write("--- Resumo Final ---\n")
    solucao_str = np.array2string(resumo['solucao'], formatter={'float_kind':lambda x: "%.5f" % x})
    file.write(f"Solucao encontrada:  {solucao_str}\n")
    file.write(f"Erro final estimado: {resumo['erro_final']:.2e}\n")
    file.write(f"Numero de iteracoes: {resumo['iteracoes']}\n")
    file.write(f"Tempo de execucao:   {tempo:.6f} segundos\n")

def gerar_relatorio_gauss(filename, A, b, resumo, tempo):
    with open(filename, "w", encoding='utf-8') as file:
        file.write("--- Relatorio do Metodo de Eliminacao de Gauss ---\n")
        file.write(f"Matriz A:\n{A}\n\n")
        file.write(f"Vetor b:\n{b}\n\n")
        
        if resumo and 'solucao' in resumo:
            solucao_str = np.array2string(resumo['solucao'], formatter={'float_kind':lambda x: "%.5f" % x})
            file.write(f"Solucao (x): {solucao_str}\n")
            file.write(f"Tempo de execucao: {tempo:.6f} segundos\n")
        else:
            file.write(f"ERRO: {resumo.get('erro_msg', 'Nao foi possivel calcular a solucao.')}\n")

def gerar_relatorio_lu(filename, A, b, resumo, tempo):
     with open(filename, "w", encoding='utf-8') as file:
        file.write("--- Relatorio do Metodo de Fatoracao LU ---\n")
        file.write(f"Matriz A:\n{A}\n\n")
        file.write(f"Vetor b:\n{b}\n\n")
        
        if resumo and 'solucao' in resumo:
            solucao_str = np.array2string(resumo['solucao'], formatter={'float_kind':lambda x: "%.5f" % x})
            file.write(f"Matriz L:\n{resumo['L']}\n\n")
            file.write(f"Matriz U:\n{resumo['U']}\n\n")
            file.write(f"Solucao (x): {solucao_str}\n")
            file.write(f"Tempo de execucao: {tempo:.6f} segundos\n")
        else:
            file.write(f"ERRO: {resumo.get('erro_msg', 'Nao foi possivel calcular a solucao.')}\n")

def gerar_relatorio_jacobi(filename, A, b, passos, resumo, tempo):
    with open(filename, "w", encoding='utf-8') as file:
        file.write("--- Relatorio do Metodo de Jacobi ---\n")
        file.write(f"Matriz A:\n{A}\n\n")
        file.write(f"Vetor b:\n{b}\n\n")
        
        file.write(f"{'Iter':>4} | {'Vetor x':<40} | {'Erro':>15}\n")
        file.write("-" * 65 + "\n")
        for p in passos:
            sol_str = np.array2string(p['x'], formatter={'float_kind':lambda x: "%.6f" % x}, max_line_width=100)
            file.write(f"{p['k']:4d} | {sol_str:<40} | {p['error']:15.6e}\n")
        
        if resumo:
            _escrever_resumo_iterativo(file, resumo, tempo)
        else:
            file.write("\nO metodo nao convergiu no numero maximo de iteracoes.\n")

def gerar_relatorio_gauss_seidel(filename, A, b, passos, resumo, tempo):
    with open(filename, "w", encoding='utf-8') as file:
        file.write("--- Relatorio do Metodo de Gauss-Seidel ---\n")
        file.write(f"Matriz A:\n{A}\n\n")
        file.write(f"Vetor b:\n{b}\n\n")
        
        file.write(f"{'Iter':>4} | {'Vetor x':<40} | {'Erro':>15}\n")
        file.write("-" * 65 + "\n")
        for p in passos:
            sol_str = np.array2string(p['x'], formatter={'float_kind':lambda x: "%.6f" % x}, max_line_width=100)
            file.write(f"{p['k']:4d} | {sol_str:<40} | {p['error']:15.6e}\n")
        
        if resumo:
            _escrever_resumo_iterativo(file, resumo, tempo)
        else:
            file.write("\nO metodo nao convergiu no numero maximo de iteracoes.\n")