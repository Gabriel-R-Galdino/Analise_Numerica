import sys
import time
import os
from sympy import symbols, sympify, lambdify, diff


def bissecao_algoritmo(F, a, b, tolerancia, maximo_iteracoes=1000):
    iteracoes = 0
    c = (a + b) / 2
    while abs(b - a) / 2 > tolerancia and iteracoes < maximo_iteracoes:
        c = (a + b) / 2
        if abs(F(c)) < 1e-15:  # Critério de parada se a função for quase zero
            break
        if F(a) * F(c) < 0:
            b = c
        else:
            a = c
        iteracoes += 1
    erro = abs(b - a) / 2
    return c, erro, iteracoes

def falsa_posicao_algoritmo(F, a, b, tolerancia, maximo_iteracoes=1000):
    iteracoes = 0
    c = a # Valor inicial para c
    while iteracoes < maximo_iteracoes:
        Fa = F(a)
        Fb = F(b)
        if abs(Fb - Fa) < 1e-15: # Evita divisão por zero
            print("AVISO: f(b) - f(a) é muito pequeno. O método pode falhar.")
            break
            
        c_novo = (a * Fb - b * Fa) / (Fb - Fa)
        Fc = F(c_novo)
        erro = abs(c_novo - c)
        c = c_novo

        if abs(Fc) < tolerancia or erro < tolerancia:
            break

        if Fa * Fc < 0:
            b = c
        else:
            a = c
        iteracoes += 1
    return c, erro, iteracoes

def newton_raphson_algoritmo(F, F_prime, a, b, tolerancia, maximo_iteracoes=1000):
    iteracoes = 0
    x = (a + b) / 2  # Chute inicial
    while iteracoes < maximo_iteracoes:
        Fx = F(x)
        F_prime_x = F_prime(x)
        
        if abs(F_prime_x) < 1e-15:
            raise ValueError("A derivada é zero ou muito próxima de zero. O método falhou.")
        
        x_new = x - Fx / F_prime_x
        erro = abs(x_new - x)
        x = x_new
        
        iteracoes += 1
        
        if erro < tolerancia or abs(Fx) < tolerancia :
            break
            
    return x, erro, iteracoes

def secante_algoritmo(F, x0, x1, tolerancia, maximo_iteracoes=1000):
    iteracoes = 0
    while iteracoes < maximo_iteracoes:
        fx0 = F(x0)
        fx1 = F(x1)

        if abs(fx1 - fx0) < 1e-15:
            print("AVISO: f(x1) - f(x0) é muito pequeno, divisão por zero evitada.")
            break

        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        erro = abs(x2 - x1)

        x0, x1 = x1, x2
        iteracoes += 1

        if erro < tolerancia:
            break

    return x2, erro, iteracoes

class ExecutorNumerico:
    """
    Classe principal que gerencia a leitura de arquivos, a execução dos
    métodos numéricos e a escrita dos resultados.
    """
    def __init__(self, filename):
        try:
            input_path = os.path.join('input', filename)
            with open(input_path, 'r') as f:
                self.func_str = f.readline().strip().replace('^', '**')
                self.a = float(f.readline().strip())
                self.b = float(f.readline().strip())
                tolerancia_str = f.readline().strip()
                self.tolerance = float(tolerancia_str) if tolerancia_str else 1e-8
            
            x = symbols('x')
            sym_func = sympify(self.func_str)
            sym_deriv = diff(sym_func, x)
            
            self.f = lambdify(x, sym_func, 'numpy')
            self.f_prime = lambdify(x, sym_deriv, 'numpy')

        except FileNotFoundError:
            print(f"\nERRO: O arquivo '{input_path}' não foi encontrado.")
            sys.exit()
        except Exception as e:
            print(f"\nOcorreu um erro ao processar o arquivo de entrada: {e}")
            sys.exit()

    def executar_metodo(self, metodo_func, nome_metodo):
        print(f"\nExecutando o método: {nome_metodo}...")
        start_time = time.time()
        
        try:
            if nome_metodo == "Newton-Raphson":
                raiz, erro, iteracoes = metodo_func(self.f, self.f_prime, self.a, self.b, self.tolerance)
            elif nome_metodo == "Secante":
                 raiz, erro, iteracoes = metodo_func(self.f, self.a, self.b, self.tolerance)
            else: # Bisseção e Posição Falsa
                if self.f(self.a) * self.f(self.b) >= 0:
                    print(f"AVISO: Não há garantia de raiz no intervalo para o método {nome_metodo}.")
                    return
                raiz, erro, iteracoes = metodo_func(self.f, self.a, self.b, self.tolerance)
            
            tempo_execucao = time.time() - start_time

            print(f"Raiz encontrada: {raiz}")
            print(f"Erro final: {erro:.2e}")
            print(f"Número de iterações: {iteracoes}")
            print(f"Tempo de execução: {tempo_execucao:.6f} segundos")

            output_filename = os.path.join("output", f"{nome_metodo.lower().replace(' ', '_')}_saida.txt")
            with open(output_filename, 'w') as f_saida:
                f_saida.write(f"Raiz encontrada: {raiz}\n")
                f_saida.write(f"Erro final: {erro}\n")
                f_saida.write(f"Numero de iteracoes: {iteracoes}\n")
                f_saida.write(f"Tempo de execucao: {tempo_execucao:.6f} segundos\n")
            print(f"Resultado salvo em '{output_filename}'")

        except Exception as e:
            print(f"Ocorreu um erro durante a execução do método {nome_metodo}: {e}")

def main():
    """Função principal que exibe o menu e gerencia a execução."""
    while True:
        print("\n--- Calculadora de Métodos Numéricos ---")
        print("1. Bissecção")
        print("2. Posição Falsa")
        print("3. Newton-Raphson")
        print("4. Secante")
        print("0. Sair")
        
        try:
            choice = int(input("Escolha uma opção: "))
            if choice == 0:
                break
            
            metodos = {
                1: (bissecao_algoritmo, "Bissecção"),
                2: (falsa_posicao_algoritmo, "Posição Falsa"),
                3: (newton_raphson_algoritmo, "Newton-Raphson"),
                4: (secante_algoritmo, "Secante")
            }
            
            if choice not in metodos:
                print("Opção inválida. Tente novamente.")
                continue

            filename = input("Digite o nome do arquivo de entrada (ex: entrada.txt): ")
            
            # Garante que as pastas de entrada e saída existam
            os.makedirs("output", exist_ok=True)
            if not os.path.exists("input"):
                print("\nERRO: A pasta 'input' não foi encontrada. Crie a pasta e coloque seu arquivo de entrada lá.")
                continue

            executor = ExecutorNumerico(filename)
            metodo_selecionado, nome_metodo = metodos[choice]
            executor.executar_metodo(metodo_selecionado, nome_metodo)

        except ValueError:
            print("\nEntrada inválida. Por favor, digite um número.")
        except KeyboardInterrupt:
            print("\nOperação cancelada. Saindo.")
            break

if __name__ == "__main__":
    main()
