import matplotlib.pyplot as plt
import os

def gerar_grafico_comparativo(metodos, tempos, filename="comparativo_tempo.png"):
    """
    Gera um gráfico de barras comparando os tempos de execução.
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
    plt.close() 
    print(f"[Gráfico] Salvo em: {path}")

def gerar_grafico_solucoes(dict_solucoes, id_problema):
    """
    Gera um gráfico de linhas comparando as trajetórias (x vs y) de cada método.
    dict_solucoes: { "NomeMetodo": ([lista_x], [lista_y]), ... }
    """
    plt.figure(figsize=(10, 6))
    
    # Estilos para diferenciar as linhas
    marcadores = ['.', 'x', 'o', 'v', '^', 's']
    estilos = ['-', '--', '-.', ':']
    
    i = 0
    for metodo, (xs, ys) in dict_solucoes.items():
        m = marcadores[i % len(marcadores)]
        ls = estilos[i % len(estilos)]
        
        # Plota apenas alguns marcadores para não poluir se tiver muitos pontos
        markevery = max(1, len(xs) // 20) 
        
        plt.plot(xs, ys, label=metodo, marker=m, markevery=markevery, 
                 linestyle=ls, alpha=0.8)
        i += 1

    plt.xlabel('X (Variável Independente)', fontsize=12)
    plt.ylabel('Y (Solução)', fontsize=12)
    plt.title(f'Comparativo de Soluções - Problema {id_problema + 1}', fontsize=14)
    plt.legend()
    plt.grid(True, which='both', linestyle='--', alpha=0.6)
    plt.tight_layout()
    
    filename = f"comparativo_solucao_prob_{id_problema + 1}.png"
    path = os.path.join("output", filename)
    plt.savefig(path, dpi=300)
    plt.close()
    print(f"[Gráfico] Solução salva em: {path}")