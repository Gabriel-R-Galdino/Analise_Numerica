import numpy as np
from sympy import Symbol, sympify, symbols

def _avaliar_funcao(func_sympy, x_val, y_val, params=None):
    """Função auxiliar para avaliar expressões sympy com dicionário de parâmetros."""
    subs_dict = {'x': x_val, 'y': y_val}
    if params:
        subs_dict.update(params)
    return float(func_sympy.subs(subs_dict).evalf())

# --- MÉTODOS DE PVI (Problema de Valor Inicial) ---

def euler_simples(func_str, y0, interval, h):
    x_sym, y_sym = symbols('x y')
    func = sympify(func_str)
    
    x_vals = [interval[0]]
    y_vals = [y0]
    
    x_current = interval[0]
    y_current = y0
    
    while round(x_current, 5) < interval[1]:
        dydx = _avaliar_funcao(func, x_current, y_current)
        y_next = y_current + h * dydx
        
        x_current += h
        y_current = y_next
        
        x_vals.append(x_current)
        y_vals.append(y_current)
        
    return x_vals, y_vals

def heun(func_str, y0, interval, h):
    x_sym, y_sym = symbols('x y')
    func = sympify(func_str)
    
    x_vals = [interval[0]]
    y_vals = [y0]
    
    x_current = interval[0]
    y_current = y0
    
    while round(x_current, 5) < interval[1]:
        # Previsão
        dydx_curr = _avaliar_funcao(func, x_current, y_current)
        y_euler = y_current + h * dydx_curr
        
        # Correção
        dydx_next = _avaliar_funcao(func, x_current + h, y_euler)
        y_next = y_current + (h / 2) * (dydx_curr + dydx_next)
        
        x_current += h
        y_current = y_next
        
        x_vals.append(x_current)
        y_vals.append(y_current)
        
    return x_vals, y_vals

def euler_modificado(func_str, y0, interval, h):
    x_sym, y_sym = symbols('x y')
    func = sympify(func_str)
    
    x_vals = [interval[0]]
    y_vals = [y0]
    x_current = interval[0]
    y_current = y0
    
    while round(x_current, 5) < interval[1]:
        k1 = _avaliar_funcao(func, x_current, y_current)
        k2 = _avaliar_funcao(func, x_current + h, y_current + h * k1)
        
        y_next = y_current + (h / 2) * (k1 + k2)
        
        x_current += h
        y_current = y_next
        
        x_vals.append(x_current)
        y_vals.append(y_current)

    return x_vals, y_vals

def ralston(func_str, y0, interval, h):
    x_sym, y_sym = symbols('x y')
    func = sympify(func_str)
    
    x_vals = [interval[0]]
    y_vals = [y0]
    x_current = interval[0]
    y_current = y0
    
    while round(x_current, 5) < interval[1]:
        k1 = _avaliar_funcao(func, x_current, y_current)
        k2 = _avaliar_funcao(func, x_current + 0.75 * h, y_current + 0.75 * h * k1)
        
        y_next = y_current + h * ((1/3)*k1 + (2/3)*k2)
        
        x_current += h
        y_current = y_next
        
        x_vals.append(x_current)
        y_vals.append(y_current)

    return x_vals, y_vals

def runge_kutta_3(func_str, y0, interval, h):
    x_sym, y_sym = symbols('x y')
    func = sympify(func_str)
    
    x_vals = [interval[0]]
    y_vals = [y0]
    x_current = interval[0]
    y_current = y0
    
    while round(x_current, 5) < interval[1]:
        k1 = _avaliar_funcao(func, x_current, y_current)
        k2 = _avaliar_funcao(func, x_current + 0.5 * h, y_current + 0.5 * h * k1)
        k3 = _avaliar_funcao(func, x_current + h, y_current - h * k1 + 2 * h * k2)
        
        y_next = y_current + (h / 6) * (k1 + 4 * k2 + k3)
        
        x_current += h
        y_current = y_next
        
        x_vals.append(x_current)
        y_vals.append(y_current)
        
    return x_vals, y_vals

def runge_kutta_4(func_str, y0, interval, h):
    x_sym, y_sym = symbols('x y')
    func = sympify(func_str)
    
    x_vals = [interval[0]]
    y_vals = [y0]
    x_current = interval[0]
    y_current = y0
    
    while round(x_current, 5) < interval[1]:
        k1 = _avaliar_funcao(func, x_current, y_current)
        k2 = _avaliar_funcao(func, x_current + 0.5 * h, y_current + 0.5 * h * k1)
        k3 = _avaliar_funcao(func, x_current + 0.5 * h, y_current + 0.5 * h * k2)
        k4 = _avaliar_funcao(func, x_current + h, y_current + h * k3)
        
        y_next = y_current + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        
        x_current += h
        y_current = y_next
        
        x_vals.append(x_current)
        y_vals.append(y_current)
        
    return x_vals, y_vals

# --- MÉTODOS DE PVC (Problema de Valor de Contorno) ---

def shooting_method(func_str, y0, interval, target, h, n, params=None):
    x_sym, y_sym = symbols('x y')
    func = sympify(func_str)
    
    # Função interna para RK4 adaptada para sistema de 2ª ordem (y' = z)
    def solve_ivp(z_guess):
        x_vals = [interval[0] + i * h for i in range(n + 1)]
        y_v = [y0]
        z_v = [z_guess]
        
        for i in range(1, len(x_vals)):
            xi, yi, zi = x_vals[i-1], y_v[i-1], z_v[i-1]
            
            # Euler simples para z 
            f_val = _avaliar_funcao(func, xi, yi, params)
            
            y_next = yi + h * zi
            z_next = zi + h * f_val
            
            y_v.append(y_next)
            z_v.append(z_next)
        return y_v[-1], x_vals, y_v

    # 1º Chute (z=0)
    y_end_1, _, _ = solve_ivp(0)
    
    # 2º Chute (z=1)
    y_end_2, _, _ = solve_ivp(1)
    
    # Interpolação Linear para achar z correto
    z_correct = 0 + (target - y_end_1) * (1 - 0) / (y_end_2 - y_end_1)
    
    # Solução final
    _, x_final, y_final = solve_ivp(z_correct)
    
    return x_final, y_final

def diferencas_finitas(func_str, y0, interval, target, h, n, params=None):
    x_sym, y_sym = symbols('x y')
    func = sympify(func_str)
    
    x_values = np.linspace(interval[0], interval[1], n + 1)
    y_values = np.zeros(n + 1)
    y_values[0] = y0
    y_values[-1] = target
    
    func_vals = []
    for i, xi in enumerate(x_values):
        val = _avaliar_funcao(func, xi, y_values[i], params)
        func_vals.append(val)
        
    A = np.zeros((n - 1, n - 1))
    b = np.zeros(n - 1)
    
    inv_h2 = 1 / h**2
    
    for i in range(1, n):
        idx = i - 1 # Índice na matriz (0 a n-2)
        
        A[idx, idx] = -2 * inv_h2
        if i > 1:
            A[idx, idx - 1] = inv_h2
        if i < n - 1:
            A[idx, idx + 1] = inv_h2
            
        b[idx] = -func_vals[i]
        
        # Ajuste para condições de contorno no vetor b
        if i == 1:
            b[idx] -= y0 * inv_h2
        if i == n - 1:
            b[idx] -= target * inv_h2

    # Resolução do Sistema
    x_solution = np.linalg.solve(A, b) # Usando numpy solve por robustez
    
    y_values[1:-1] = x_solution
    
    return x_values, y_values