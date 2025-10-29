from sympy import Symbol, expand
import numpy as np

def lagrange_polynomial(x_values, y_values):
    """Calcula o polinômio de Lagrange."""
    x = Symbol('x')
    n = len(x_values)
    lagrange_poly = 0

    for i in range(n):
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x - x_values[j]) / (x_values[i] - x_values[j])
        lagrange_poly += L_i * y_values[i]

    return expand(lagrange_poly)

def newton_divided_differences(x_values, y_values):
    """Calcula o polinômio de Newton por diferenças divididas."""
    n = len(x_values)
    # Tabela de diferenças divididas
    diferencas_div = np.zeros((n, n))
    diferencas_div[:, 0] = y_values

    for j in range(1, n):
        for i in range(n - j):
            diferencas_div[i][j] = (diferencas_div[i + 1][j - 1] - diferencas_div[i][j - 1]) / (x_values[i + j] - x_values[i])

    # Construção do polinômio
    newton_poly = diferencas_div[0][0]
    x = Symbol('x')
    for j in range(1, n):
        termo = diferencas_div[0][j]
        for i in range(j):
            termo *= (x - x_values[i])
        newton_poly += termo

    return expand(newton_poly)