import math

def _function(x_value, f_str):
    """Função auxiliar para avaliar a string da função."""
    # Mantém a lógica original do eval
    return eval(f_str, {"x": x_value, "math": math})

def finite_difference_first_order(func_str, x_value):
    """Calcula a derivada de 1ª ordem."""
    h = 1.0  # Valor de h do seu código original
    
    func_plus_h = _function(x_value + h, func_str)
    func_minus_h = _function(x_value - h, func_str)
    
    d = (func_plus_h - func_minus_h) / (2 * h)
    return d

def finite_difference_second_order(func_str, x_value):
    """Calcula a derivada de 2ª ordem."""
    h = 0.1  # Valor de h do seu código original
    
    func_plus_h = _function(x_value + h, func_str)
    func_minus_h = _function(x_value - h, func_str)
    func_at_x = _function(x_value, func_str)
    
    d = (func_plus_h - 2 * func_at_x + func_minus_h) / (h ** 2)
    return d