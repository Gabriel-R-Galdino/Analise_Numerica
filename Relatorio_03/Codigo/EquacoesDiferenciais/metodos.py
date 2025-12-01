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
        # Previsão (Euler)
        dydx_curr = _avaliar_funcao(func, x_current, y_current)
        y_euler = y_current + h * dydx_curr
        
        # Correção (Heun)
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
    
    # Parâmetros de iteração
    tol = 1e-5
    max_iter = 100
    
    # Função interna para resolver o PVI usando RK4 (Sistema de 2ª ordem)
    # y' = z
    # z' = f(x, y)
    def solve_ivp_rk4(z_initial):
        x_vals = [interval[0]]
        y_vals = [y0]
        z_vals = [z_initial] # z é a derivada dy/dx
        
        x_curr = interval[0]
        y_curr = y0
        z_curr = z_initial
        
        
        while round(x_curr, 5) < interval[1]:
            # K1
            k1_y = z_curr
            k1_z = _avaliar_funcao(func, x_curr, y_curr, params)
            
            # K2
            k2_y = z_curr + 0.5 * h * k1_z
            # Nota: para k2_z, o y muda. Se a função dependesse de z, o z mudaria também.
            k2_z = _avaliar_funcao(func, x_curr + 0.5*h, y_curr + 0.5*h*k1_y, params)
            
            # K3
            k3_y = z_curr + 0.5 * h * k2_z
            k3_z = _avaliar_funcao(func, x_curr + 0.5*h, y_curr + 0.5*h*k2_y, params)
            
            # K4
            k4_y = z_curr + h * k3_z
            k4_z = _avaliar_funcao(func, x_curr + h, y_curr + h*k3_y, params)
            
            # Atualiza
            y_next = y_curr + (h/6) * (k1_y + 2*k2_y + 2*k3_y + k4_y)
            z_next = z_curr + (h/6) * (k1_z + 2*k2_z + 2*k3_z + k4_z)
            x_next = x_curr + h
            
            x_curr = x_next
            y_curr = y_next
            z_curr = z_next
            
            x_vals.append(x_curr)
            y_vals.append(y_curr)
            
        return y_vals[-1], x_vals, y_vals

    # --- Processo Iterativo (Shooting) ---
    
    # Chute 0
    s0 = 0.0 # Chute inicial para derivada
    y_end0, _, _ = solve_ivp_rk4(s0)
    erro0 = y_end0 - target
    
    # Chute 1
    s1 = 1.0 # Segundo chute
    y_end1, _, _ = solve_ivp_rk4(s1)
    erro1 = y_end1 - target
    
    iter_count = 0
    
    # Loop da Secante para encontrar o s correto
    s_curr = s1
    
    while abs(erro1) > tol and iter_count < max_iter:
        if (erro1 - erro0) == 0:
            print("Aviso: Divisão por zero no método Shooting. Tentando perturbação.")
            s_new = s1 + 0.1
        else:
            # Fórmula da Secante para encontrar novo chute de derivada
            s_new = s1 - erro1 * (s1 - s0) / (erro1 - erro0)
        
        y_end_new, xs_new, ys_new = solve_ivp_rk4(s_new)
        erro_new = y_end_new - target
        
        # Atualiza variáveis para próxima iteração
        s0, erro0 = s1, erro1
        s1, erro1 = s_new, erro_new
        s_curr = s_new
        
        iter_count += 1
        
    # Roda uma última vez com o melhor s encontrado para retornar as listas
    _, x_final, y_final = solve_ivp_rk4(s_curr)
    
    return x_final, y_final

def diferencas_finitas(func_str, y0, interval, target, h, n, params=None):
    x_sym, y_sym = symbols('x y')
    func = sympify(func_str)
    
    x_values = np.linspace(interval[0], interval[1], n + 1)
    
    y_guess = np.linspace(y0, target, n + 1)
    
    func_vals = []
    for i, xi in enumerate(x_values):
        # Usa o y_guess[i] em vez de 0.0
        val = _avaliar_funcao(func, xi, y_guess[i], params)
        func_vals.append(val)
        
    A = np.zeros((n - 1, n - 1))
    b = np.zeros(n - 1)
    
    inv_h2 = 1 / h**2
    
    for i in range(1, n):
        idx = i - 1 
        
        A[idx, idx] = -2 * inv_h2
        if i > 1:
            A[idx, idx - 1] = inv_h2
        if i < n - 1:
            A[idx, idx + 1] = inv_h2
            
        b[idx] = func_vals[i]
        
        # Ajuste para condições de contorno no vetor b
        if i == 1:
            b[idx] -= y0 * inv_h2
        if i == n - 1:
            b[idx] -= target * inv_h2

    # Resolução do Sistema
    try:
        x_solution = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        print("Erro: Matriz singular ou mal condicionada.")
        return x_values, np.zeros_like(x_values)
    
    y_values = np.zeros(n + 1)
    y_values[0] = y0
    y_values[-1] = target
    y_values[1:-1] = x_solution
    
    return x_values, y_values