import numpy as np
from sympy import Symbol, sympify, integrate, zeros, E, expand

def linear_regression(values_x, values_y):
    """Executa a Regressão Linear."""
    x_sum = sum(values_x)
    y_sum = sum(values_y)
    xy_sum = sum(x * y for x, y in zip(values_x, values_y))
    x_squared_sum = sum(x**2 for x in values_x)
    n = len(values_x)

    b = (n * xy_sum - x_sum * y_sum) / (n * x_squared_sum - x_sum**2)
    a = (y_sum - b * x_sum) / n
    
    # Retorna os coeficientes
    return round(a, 2), round(b, 2)

def discrete_polynomial_approximation(values_x, values_y):
    """Executa a Aproximação Polinomial Discreta (Grau 2)."""
    x = Symbol("x")
    basis_functions = [1, x, x**2]
    num_functions = len(basis_functions)
    num_values = len(values_x)
    
    matrix_Ui = [[1] * num_values]
    for func in basis_functions[1:]:
        row = [func.subs(x, value) for value in values_x]
        matrix_Ui.append(row)

    vector_F = np.zeros((num_functions, 1))
    matrix_M = np.zeros((num_functions, num_functions))
    
    for i in range(num_functions):
        for j in range(num_functions):
            matrix_M[i, j] = sum(np.multiply(matrix_Ui[i], matrix_Ui[j]))
        vector_F[i, 0] = sum(np.multiply(values_y, matrix_Ui[i]))

    solution = np.linalg.solve(matrix_M, vector_F)
    result_expression = sum(round(solution[i, 0], 2) * x**i for i in range(num_functions))
    
    return expand(result_expression)

def continuous_polynomial_approximation(func_str, interval):
    """Executa a Aproximação Polinomial Contínua (Grau 2)."""
    x = Symbol("x")
    basis_functions = [1, x, x**2]
    num_basis = len(basis_functions)
    
    # Converte a string da função em uma função sympy
    locals_dict = {"e": E, "x": x}
    processed_str = func_str.replace('^', '**').replace('math.e', 'e')
    func = sympify(processed_str, locals=locals_dict)

    matrix_M = zeros(num_basis)
    vector_F = zeros(num_basis, 1)
    
    for i in range(num_basis):
        for j in range(num_basis):
            integrand_M = basis_functions[i] * basis_functions[j]
            matrix_M[i, j] = integrate(integrand_M, (x, interval[0], interval[1]))
        
        integrand_F = basis_functions[i] * func
        vector_F[i, 0] = integrate(integrand_F, (x, interval[0], interval[1]))

    coefficients = matrix_M.LUsolve(vector_F)
    
    approx_expression = sum(round(coefficients[i, 0], 5) * basis_functions[i] for i in range(num_basis))
    return expand(approx_expression)