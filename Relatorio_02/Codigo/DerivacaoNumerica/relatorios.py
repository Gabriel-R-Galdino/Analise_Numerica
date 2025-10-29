def _escrever_sumario_tempo(file, tempo):
    file.write("\n" + "-"*50 + "\n")
    file.write(f"Tempo de execucao: {tempo:.6f} segundos\n")

def gerar_relatorio_derivacao(filename, titulo_metodo, funcoes, results, tempo):
    """Gera o relatório para métodos de Derivação."""
    with open(filename, "w", encoding='utf-8') as file:
        file.write(f"--- Relatório de {titulo_metodo} ---\n\n")
        
        for idx, res in enumerate(results):
            file.write(f"Derivada da função {idx+1} ({funcoes[idx]}): {res}\n")
            
        _escrever_sumario_tempo(file, tempo)