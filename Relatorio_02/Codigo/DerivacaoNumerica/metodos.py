import math
import numpy as np

def _function(x_value, f_str):
    """Função auxiliar para avaliar a string da função."""
    allowed_names = {
        'x': x_value,
        'sin': np.sin,
        'cos': np.cos,
        'tan': np.tan,
        'exp': np.exp,
        'log': np.log,
        'sqrt': np.sqrt,
        'pi': np.pi,
        'e': np.e,
        'abs': abs,
        'pow': pow,
    }
    return eval(f_str, {"__builtins__": None}, allowed_names)

def finite_difference_first_order(func_str, x_value):
    """Calcula a derivada de 1ª ordem."""
    h = 1e-5  
    
    func_plus_h = _function(x_value + h, func_str)
    func_minus_h = _function(x_value - h, func_str)
    
    d = (func_plus_h - func_minus_h) / (2 * h)
    return d

def finite_difference_second_order(func_str, x_value):
    """Calcula a derivada de 2ª ordem."""
    h = 1e-5 
    
    func_plus_h = _function(x_value + h, func_str)
    func_minus_h = _function(x_value - h, func_str)
    func_at_x = _function(x_value, func_str)
    
    d = (func_plus_h - 2 * func_at_x + func_minus_h) / (h ** 2)
    return d