import matplotlib.pyplot as plt
import os

def gerar_grafico_comparativo(metodos, tempos, filename="comparativo_tempo.png"):
    """
    Gera um gráfico de barras comparando os tempos de execução.
    metodos: Lista de strings com os nomes dos métodos.
    tempos: Lista de floats com os tempos de execução.
    """
    plt.figure(figsize=(10, 6))
    
    # Criar barras
    bars = plt.bar(metodos, tempos, color='skyblue', edgecolor='black')
    
    # Adicionar rótulos e títulos
    plt.xlabel('Métodos Numéricos', fontsize=12)
    plt.ylabel('Tempo de Execução (segundos)', fontsize=12)
    plt.title('Comparativo de Desempenho Computacional', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Adicionar o valor do tempo em cima de cada barra
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.5f}s', 
                 ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    
    # Salvar na pasta output
    path = os.path.join("output", filename)
    plt.savefig(path)
    plt.close() # Fecha a figura para liberar memória
    print(f"\n[Gráfico] Salvo em: {path}")