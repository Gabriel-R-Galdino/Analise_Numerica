"""
Módulo contendo a implementação dos algoritmos numéricos.
Cada função retorna uma tupla: (lista de passos, dicionário de resumo).
"""

def bissecao(f, a, b, tolerance):
    """Executa o método da Bisseção."""
    if f(a) * f(b) >= 0:
        return None, None # Sinaliza que não há garantia de raiz

    passos = []
    for k in range(1, 1001):
        c = (a + b) / 2
        f_c = f(c)
        error = abs(b - a)
        
        passos.append({'k': k, 'a': a, 'b': b, 'c': c, 'f_c': f_c, 'error': error})

        if error / 2 < tolerance or abs(f_c) < 1e-15:
            resumo = {'raiz': c, 'erro_final': error / 2, 'iteracoes': k}
            return passos, resumo

        if f(a) * f_c < 0:
            b = c
        else:
            a = c
            
    return passos, None # Não convergiu

def falsa_posicao(f, a, b, tolerance):
    """Executa o método da Posição Falsa."""
    if f(a) * f(b) >= 0:
        return None, None

    passos = []
    c_old = float('inf')
    for k in range(1, 1001):
        f_a, f_b = f(a), f(b)
        c = (a * f_b - b * f_a) / (f_b - f_a)
        f_c = f(c)
        error = abs(c - c_old)
        
        passos.append({'k': k, 'a': a, 'b': b, 'c': c, 'f_c': f_c, 'error': error})
        
        if error < tolerance or abs(f_c) < 1e-15:
            resumo = {'raiz': c, 'erro_final': error, 'iteracoes': k}
            return passos, resumo
        
        if f_a * f_c < 0:
            b = c
        else:
            a = c
        c_old = c
        
    return passos, None

def newton_raphson(f, f_prime, x0, tolerance):
    """Executa o método de Newton-Raphson."""
    passos = []
    x = x0
    for k in range(1, 1001):
        f_x = f(x)
        f_prime_x = f_prime(x)

        if abs(f_prime_x) < 1e-12:
            return passos, {'erro_msg': 'Derivada próxima de zero.'}

        x_new = x - f_x / f_prime_x
        error = abs(x_new - x)
        
        passos.append({'k': k, 'x_i': x, 'f_x_i': f_x, 'f_prime_x_i': f_prime_x, 'error': error})
        
        if error < tolerance or abs(f_x) < 1e-15:
            resumo = {'raiz': x_new, 'erro_final': error, 'iteracoes': k}
            return passos, resumo
        
        x = x_new

    return passos, None

def secante(f, x0, x1, tolerance):
    """Executa o método da Secante."""
    passos = []
    for k in range(1, 1001):
        f_x0, f_x1 = f(x0), f(x1)
        
        if abs(f_x1 - f_x0) < 1e-12:
            return passos, {'erro_msg': 'Divisão por valor muito pequeno.'}
        
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        error = abs(x2 - x1)
        
        passos.append({'k': k, 'x_i+1': x2, 'f_x_i+1': f(x2), 'error': error})

        if error < tolerance or abs(f(x2)) < 1e-15:
            resumo = {'raiz': x2, 'erro_final': error, 'iteracoes': k}
            return passos, resumo
        
        x0, x1 = x1, x2
        
    return passos, None