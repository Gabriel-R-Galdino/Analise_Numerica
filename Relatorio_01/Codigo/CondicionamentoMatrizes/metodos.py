"""
Módulo contendo a implementação dos algoritmos de análise de matrizes.
"""
import numpy as np

def fatoracao_lu(A):
    """Executa a fatoração LU em uma matriz A."""
    n = A.shape[0]
    L = np.eye(n)
    U = A.copy().astype(float)

    for i in range(n):
        for j in range(i + 1, n):
            if U[i, i] == 0:
                raise np.linalg.LinAlgError("Pivô nulo encontrado. A fatoração LU sem pivoteamento não é possível.")
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j] -= factor * U[i]
    return L, U

def inversa(A):
    """Calcula a inversa de uma matriz A usando a fatoração LU."""
    L, U = fatoracao_lu(A)
    n = A.shape[0]
    A_inv = np.zeros((n, n))

    for i in range(n):
        b = np.zeros(n)
        b[i] = 1
        
        # Solução de Ly = b
        y = np.zeros(n)
        for j in range(n):
            y[j] = b[j] - np.dot(L[j, :j], y[:j])
        
        # Solução de Ux = y
        x = np.zeros(n)
        for j in range(n - 1, -1, -1):
            x[j] = (y[j] - np.dot(U[j, j + 1:], x[j + 1:])) / U[j, j]
        
        A_inv[:, i] = x
        
    return A_inv

def numero_condicao(A):
    """Calcula o número de condição da matriz A, sua inversa e normas associadas."""
    try:
        norma_A = np.linalg.norm(A, ord=2)
        A_inversa = inversa(A)
        norma_A_inversa = np.linalg.norm(A_inversa, ord=2)
        
        cond_num = norma_A * norma_A_inversa
        
        resumo = {
            'numero_condicao': cond_num,
            'inversa': A_inversa,
            'norma_A': norma_A,
            'norma_A_inversa': norma_A_inversa
        }
        return resumo
        
    except np.linalg.LinAlgError as e:
        return {'erro_msg': f"Erro no cálculo: a matriz pode ser singular. ({e})"}