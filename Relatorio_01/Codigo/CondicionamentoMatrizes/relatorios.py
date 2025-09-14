"""
Módulo para geração de relatórios de saída.
"""
import numpy as np

def gerar_relatorio_condicao(filename, A, resumo, tempo):
    """Gera um relatório detalhado sobre o condicionamento da matriz A."""
    with open(filename, "w", encoding='utf-8') as file:
        file.write("--- Relatório de Análise de Condicionamento de Matriz ---\n\n")
        file.write(f"Matriz Original A:\n{np.array2string(A, formatter={'float_kind':lambda x: '%.4f' % x})}\n\n")
        file.write("-" * 60 + "\n")
        
        if 'erro_msg' in resumo:
            file.write(f"ERRO: {resumo['erro_msg']}\n")
            return

        file.write(f"Norma da Matriz A (norma-inf): {resumo['norma_A']:.5f}\n")
        file.write(f"Número de Condição K(A):        {resumo['numero_condicao']:.5f}\n")
        
        if resumo['numero_condicao'] > 100: # Limiar arbitrário
            file.write("-> AVISO: A matriz é considerada mal condicionada.\n")
        else:
            file.write("-> A matriz é considerada bem condicionada.\n")
            
        file.write("\n" + "-" * 60 + "\n")
        file.write("Matriz Inversa A⁻¹:\n")
        file.write(np.array2string(resumo['inversa'], formatter={'float_kind':lambda x: '%.5f' % x}))
        file.write(f"\n\nNorma da Matriz Inversa (norma-inf): {resumo['norma_A_inversa']:.5f}\n")
        
        file.write("\n" + "-" * 60 + "\n")
        file.write(f"Tempo de execução: {tempo:.6f} segundos\n")