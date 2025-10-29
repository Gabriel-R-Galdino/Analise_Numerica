def _escrever_sumario_tempo(file, tempo):
    file.write("\n" + "-"*50 + "\n")
    file.write(f"Tempo de execucao: {tempo:.6f} segundos\n")

def gerar_relatorio_interpolacao(filename, titulo_metodo, results, tempo):
    """Gera o relatório para métodos de Interpolação."""
    with open(filename, "w", encoding='utf-8') as file:
        file.write(f"--- Relatório de {titulo_metodo} ---\n\n")
        
        for idx, poly_expr in enumerate(results):
            file.write(f"Conjunto {idx+1}: {poly_expr}\n")
            
        _escrever_sumario_tempo(file, tempo)