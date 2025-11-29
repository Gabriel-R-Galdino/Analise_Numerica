def _escrever_sumario_tempo(file, tempo):
    file.write("\n" + "-"*50 + "\n")
    file.write(f"Tempo de execucao: {tempo:.6f} segundos\n")

def gerar_relatorio_edo(filename, titulo_metodo, results, tempo):
    """
    Gera relatório para PVI (Euler, RK, etc) e PVC (Shooting, Diferenças Finitas).
    results: Lista de tuplas (vetor_x, vetor_y)
    """
    with open(filename, "w", encoding='utf-8') as file:
        file.write(f"--- Relatório: {titulo_metodo} ---\n\n")
        
        for idx, (x_vals, y_vals) in enumerate(results):
            file.write(f"Problema {idx + 1}:\n")
            
            # Se for array numpy, converte para lista para garantir zip correto
            if hasattr(x_vals, 'tolist'): x_vals = x_vals.tolist()
            if hasattr(y_vals, 'tolist'): y_vals = y_vals.tolist()

            for x, y in zip(x_vals, y_vals):
                file.write(f"x = {x:.5f}, y = {y:.5f}\n")
            file.write("\n")
            
        _escrever_sumario_tempo(file, tempo)