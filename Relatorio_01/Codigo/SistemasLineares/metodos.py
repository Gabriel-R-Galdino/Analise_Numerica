"""
Módulo contendo a implementação dos algoritmos de sistemas lineares.
"""
import numpy as np

def _make_diagonally_dominant(A_in, b_in):
    """
    Função auxiliar para reorganizar A e b para garantir a dominância diagonal,
    essencial para a convergência de métodos iterativos.
    """
    A = A_in.copy()
    b = b_in.copy()
    n = len(b)
    for i in range(n):
        pivot_row = i + np.argmax(np.abs(A[i:, i]))
        if pivot_row != i:
            A[[i, pivot_row]] = A[[pivot_row, i]]
            b[[i, pivot_row]] = b[[pivot_row, i]]
    return A, b

def eliminacao_gauss(A_in, b_in):
    """Executa o método de Eliminação de Gauss."""
    A = A_in.copy().astype(float)
    b = b_in.copy().astype(float)
    n = len(b)

    for i in range(n):
        # Pivoteamento parcial para estabilidade numérica
        pivot_row = i + np.argmax(np.abs(A[i:, i]))
        if pivot_row != i:
            A[[i, pivot_row]] = A[[pivot_row, i]]
            b[[i, pivot_row]] = b[[pivot_row, i]]

        if A[i, i] == 0:
            return None, {'erro_msg': 'Matriz singular detectada.'}

        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    x[np.abs(x) < 1e-12] = 0.0
    resumo = {'solucao': x}
    return resumo

def fatoracao_lu(A_in, b_in):
    """Executa o método da Fatoração LU."""
    A = A_in.copy().astype(float)
    b = b_in.copy().astype(float)
    n = len(b)
    
    if np.linalg.det(A) == 0:
        return None, {'erro_msg': 'Matriz singular, não pode ser decomposta.'}

    L = np.eye(n)
    U = A.copy()

    for i in range(n):
        for j in range(i + 1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j] -= factor * U[i]

    # Solução de Ly = b
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    # Solução de Ux = y
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]
        
    x[np.abs(x) < 1e-12] = 0.0
    resumo = {'solucao': x, 'L': L, 'U': U}
    return resumo

def jacobi(A_in, b_in, max_iterations=1000, tolerance=1e-6):
    """Executa o método iterativo de Jacobi."""
    A, b = _make_diagonally_dominant(A_in, b_in)
    n = len(b)
    x = np.zeros(n)
    passos = []

    for k in range(1, max_iterations + 1):
        x_new = np.zeros(n)
        for i in range(n):
            sum_ax = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - sum_ax) / A[i, i]
        
        error = np.linalg.norm(x_new - x)
        passos.append({'k': k, 'x': x_new.copy(), 'error': error})

        if error < tolerance:
            resumo = {'solucao': x_new, 'iteracoes': k, 'erro_final': error}
            return passos, resumo
        
        x = x_new.copy()

    return passos, None # Não convergiu

def gauss_seidel(A_in, b_in, max_iterations=1000, tolerance=1e-6):
    """Executa o método iterativo de Gauss-Seidel."""
    A, b = _make_diagonally_dominant(A_in, b_in)
    n = len(b)
    x = np.zeros(n)
    passos = []

    for k in range(1, max_iterations + 1):
        x_old = x.copy()
        for i in range(n):
            sum_ax1 = np.dot(A[i, :i], x[:i]) # Usa valores já atualizados de x
            sum_ax2 = np.dot(A[i, i+1:], x_old[i+1:]) # Usa valores da iteração anterior
            x[i] = (b[i] - sum_ax1 - sum_ax2) / A[i, i]
            
        error = np.linalg.norm(x - x_old)
        passos.append({'k': k, 'x': x.copy(), 'error': error})
        
        if error < tolerance:
            resumo = {'solucao': x, 'iteracoes': k, 'erro_final': error}
            return passos, resumo

    return passos, None # Não convergiu