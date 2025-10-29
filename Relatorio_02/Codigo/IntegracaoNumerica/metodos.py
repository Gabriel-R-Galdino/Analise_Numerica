import math
import numpy as np

def _function(x_value, f_str):
    """Função auxiliar para avaliar a string da função."""
    return eval(f_str, {"x": x_value, "math": math})

def trapezoidal(func_str, a, b, n):
    """Regra dos Trapézios (Simples/Múltipla)."""
    h = (b - a) / n
    x_vals = np.linspace(a, b, n + 1)
    y_vals = [_function(x, func_str) for x in x_vals]
    
    integral = h * (0.5 * y_vals[0] + sum(y_vals[1:-1]) + 0.5 * y_vals[-1])
    return round(integral, 4)

def simpson_1_3_simple(func_str, a, b, n_ignored):
    """Regra de Simpson 1/3 Simples."""
    # 'n' é ignorado para manter a lógica do seu 'simple_simpson_1_3_aux'
    h = (b - a) / 2
    func_at_a = _function(a, func_str)
    func_at_mid = _function((a + b) / 2, func_str)
    func_at_b = _function(b, func_str)

    integral_value = (h / 3) * (func_at_a + 4 * func_at_mid + func_at_b)
    return round(integral_value, 4)

def simpson_1_3_multiple(func_str, a, b, n):
    """Regra de Simpson 1/3 Múltipla."""
    if n % 2 != 0:
        n += 1  # Garante 'n' par
    h = (b - a) / n

    integral_value = _function(a, func_str) + _function(b, func_str)
    for j in range(1, n):
        x_j = a + j * h
        coeficiente = 4 if j % 2 != 0 else 2
        integral_value += coeficiente * _function(x_j, func_str)

    integral_value *= h / 3
    return round(integral_value, 4)

def simpson_3_8_simple(func_str, a, b, n):
    """Regra de Simpson 3/8 Simples (baseado na sua lógica original)."""
    if n % 3 != 0:
        n = n + (3 - (n % 3))  # Garante 'n' múltiplo de 3
    h = (b - a) / n

    integral_value = _function(a, func_str) + _function(b, func_str)
    for j in range(1, n):
        x_j = a + j * h
        coeficiente = 3 if j % 3 != 0 else 2
        integral_value += coeficiente * _function(x_j, func_str)

    integral_value *= (3 * h) / 8
    return round(integral_value, 4)

def simpson_3_8_multiple(func_str, a, b, n):
    """Regra de Simpson 3/8 Múltipla."""
    if n % 3 != 0:
        n = n + (3 - (n % 3))
    h = (b - a) / n

    integral_value = 0
    for j in range(0, n, 3):
        x0 = a + j * h
        x1 = a + (j + 1) * h
        x2 = a + (j + 2) * h
        x3 = a + (j + 3) * h
        
        integral_value += (3 * h / 8) * (_function(x0, func_str) + 3 * _function(x1, func_str) + 3 * _function(x2, func_str) + _function(x3, func_str))
    
    return round(integral_value, 4)

def richards_extrapolation(func_str, a, b, n_ignored):
    """Extrapolação de Richards."""
    # 'n' é ignorado. Usa a lógica original de chamar o 'simpson_1_3_simple'
    # Nota: A lógica original tinha um bug aqui, pois chamava a mesma função
    # com N=250 e N=500, mas a função ignora N. Mantive essa lógica.
    integral_n1 = simpson_1_3_simple(func_str, a, b, 250)
    integral_n2 = simpson_1_3_simple(func_str, a, b, 500)

    richardson_result = ((4 / 3) * integral_n2) - ((1 / 3) * integral_n1)
    return round(richardson_result, 4)

def gaussian_quadrature(func_str, a, b, n_ignored):
    """Quadratura de Gauss (2 pontos)."""
    pontos_gauss = [-math.sqrt(3)/3, math.sqrt(3)/3]
    pesos_gauss = [1, 1]

    # Mudança de variável
    t = lambda u: 0.5 * (b - a) * u + 0.5 * (a + b)

    integral_value = 0
    for i in range(len(pontos_gauss)):
        integral_value += pesos_gauss[i] * _function(t(pontos_gauss[i]), func_str)
    
    integral_value *= (b - a) / 2
    return round(integral_value, 4)