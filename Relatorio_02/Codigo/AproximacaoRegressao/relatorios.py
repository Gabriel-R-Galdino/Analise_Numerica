def _escrever_sumario_tempo(file, tempo):
    file.write("\n" + "-"*50 + "\n")
    file.write(f"Tempo de execucao: {tempo:.6f} segundos\n")

def gerar_relatorio_regressao_linear(filename, results, tempo):
    """Gera o relatório para Regressão Linear."""
    with open(filename, "w", encoding='utf-8') as file:
        file.write("--- Relatório de Regressão Linear ---\n\n")
        
        for idx, res in enumerate(results):
            b, a = res['b'], res['a']
            # Lógica de formatação do seu arquivo original
            result_str = f"y = {b}*x + {a}" if a >= 0 else f"y = {b}*x - {abs(a)}"
            file.write(f"Conjunto {idx+1}: {result_str}\n")
            
        _escrever_sumario_tempo(file, tempo)

def gerar_relatorio_aprox_polinomial(filename, titulo_metodo, results, tempo):
    """Gera o relatório para Aproximações Polinomiais."""
    with open(filename, "w", encoding='utf-8') as file:
        file.write(f"--- Relatório de {titulo_metodo} ---\n\n")
        
        for idx, poly_expr in enumerate(results):
            file.write(f"Função {idx+1}: y = {poly_expr}\n")
            
        _escrever_sumario_tempo(file, tempo)