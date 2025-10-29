def _escrever_sumario_tempo(file, tempo):
    file.write("\n" + "-"*50 + "\n")
    file.write(f"Tempo de execucao: {tempo:.6f} segundos\n")

def gerar_relatorio_integracao(filename, titulo_metodo, results, tempo):
    """Gera o relatório genérico para métodos de Integração."""
    with open(filename, "w", encoding='utf-8') as file:
        file.write(f"--- Relatório de {titulo_metodo} ---\n\n")
        
        for idx, res in enumerate(results):
            file.write(f"Integral da função {idx+1}: {res}\n")
            
        _escrever_sumario_tempo(file, tempo)