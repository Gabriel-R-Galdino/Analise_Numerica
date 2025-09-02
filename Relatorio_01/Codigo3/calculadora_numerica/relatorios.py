
"""
Módulo para geração de relatórios de saída.
"""

def _escrever_resumo(file, resumo, tempo):
    """Escreve o bloco de resumo final no arquivo de relatório."""
    file.write("\n" + "-"*75 + "\n")
    file.write("--- Resumo Final ---\n")
    file.write(f"Raiz encontrada:     {resumo['raiz']:.8f}\n")
    file.write(f"Erro final estimado: {resumo['erro_final']:.2e}\n")
    file.write(f"Numero de iteracoes: {resumo['iteracoes']}\n")
    file.write(f"Tempo de execucao:   {tempo:.6f} segundos\n")

def gerar_relatorio_bissecao(filename, func_str, passos, resumo, tempo):
    with open(filename, "w", encoding='utf-8') as file:
        file.write(f"--- Relatorio do Metodo da Bissecao ---\n")
        file.write(f"Funcao: f(x) = {func_str}\n\n")
        file.write(f"{'Iter':>4} | {'a':>12} | {'b':>12} | {'c (raiz)':>12} | {'f(c)':>15} | {'Erro |b-a|':>15}\n")
        file.write("-" * 75 + "\n")
        for p in passos:
            file.write(f"{p['k']:4d} | {p['a']:12.6f} | {p['b']:12.6f} | {p['c']:12.6f} | {p['f_c']:15.6e} | {p['error']:15.6e}\n")
        if resumo:
            _escrever_resumo(file, resumo, tempo)

def gerar_relatorio_falsa_posicao(filename, func_str, passos, resumo, tempo):
    with open(filename, "w", encoding='utf-8') as file:
        file.write(f"--- Relatorio do Metodo da Posicao Falsa ---\n")
        file.write(f"Funcao: f(x) = {func_str}\n\n")
        file.write(f"{'Iter':>4} | {'a':>12} | {'b':>12} | {'c (raiz)':>12} | {'f(c)':>15} | {'Erro |c-c_old|':>18}\n")
        file.write("-" * 80 + "\n")
        for p in passos:
            file.write(f"{p['k']:4d} | {p['a']:12.6f} | {p['b']:12.6f} | {p['c']:12.6f} | {p['f_c']:15.6e} | {p['error']:18.6e}\n")
        if resumo:
            _escrever_resumo(file, resumo, tempo)

def gerar_relatorio_newton(filename, func_str, x0, passos, resumo, tempo):
    with open(filename, "w", encoding='utf--8') as file:
        file.write(f"--- Relatorio do Metodo de Newton-Raphson ---\n")
        file.write(f"Funcao: f(x) = {func_str}\n")
        file.write(f"Chute inicial: x0 = {x0:.6f}\n\n")
        file.write(f"{'Iter':>4} | {'x_i':>15} | {'f(x_i)':>15} | {"f'(x_i)":>15} | {'Erro |x_i-x_i-1|':>20}\n")
        file.write("-" * 78 + "\n")
        for p in passos:
            file.write(f"{p['k']:4d} | {p['x_i']:15.8f} | {p['f_x_i']:15.6e} | {p['f_prime_x_i']:15.6e} | {p['error']:20.6e}\n")
        if resumo and 'erro_msg' not in resumo:
            _escrever_resumo(file, resumo, tempo)
        elif resumo:
            file.write(f"\nERRO: {resumo['erro_msg']}\n")

def gerar_relatorio_secante(filename, func_str, x0, x1, passos, resumo, tempo):
    with open(filename, "w", encoding='utf-8') as file:
        file.write(f"--- Relatorio do Metodo da Secante ---\n")
        file.write(f"Funcao: f(x) = {func_str}\n")
        file.write(f"Pontos iniciais: x0 = {x0}, x1 = {x1}\n\n")
        file.write(f"{'Iter':>4} | {'x_i+1':>15} | {'f(x_i+1)':>15} | {'Erro |x_i+1 - x_i|':>22}\n")
        file.write("-" * 65 + "\n")
        for p in passos:
            file.write(f"{p['k']:4d} | {p['x_i+1']:15.8f} | {p['f_x_i+1']:15.6e} | {p['error']:22.6e}\n")
        if resumo and 'erro_msg' not in resumo:
            _escrever_resumo(file, resumo, tempo)
        elif resumo:
            file.write(f"\nERRO: {resumo['erro_msg']}\n")