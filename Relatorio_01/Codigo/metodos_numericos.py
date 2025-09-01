import sys
import time
import os
from sympy import symbols, sympify, lambdify, diff

class CalculadoraNumerica:
    """
    Classe que encapsula métodos numéricos para encontrar raízes de funções,
    gerando relatórios detalhados para cada execução.
    """
    def __init__(self, filename):
        """
        Inicializa o objeto lendo e processando o arquivo de entrada da pasta 'input'.
        """
        try:
            input_path = os.path.join('input', filename)
            with open(input_path, 'r', encoding='utf-8') as f:
                self.func_str = f.readline().strip()
                self.a = float(f.readline().strip())
                self.b = float(f.readline().strip())
                tolerancia_str = f.readline().strip()
                self.tolerance = float(tolerancia_str) if tolerancia_str else 1e-8
            
            x = symbols('x')
            safe_func_str = self.func_str.replace('^', '**')
            
            sym_func = sympify(safe_func_str)
            sym_deriv = diff(sym_func, x)
            
            self.f = lambdify(x, sym_func, 'numpy')
            self.f_prime = lambdify(x, sym_deriv, 'numpy')

        except FileNotFoundError:
            print(f"\nERRO: O arquivo '{input_path}' não foi encontrado.")
            sys.exit()
        except Exception as e:
            print(f"\nOcorreu um erro ao processar o arquivo de entrada: {e}")
            sys.exit()

    def _escrever_resumo(self, file, raiz, erro, iteracoes, tempo):
        """Escreve o bloco de resumo final no arquivo de relatório."""
        file.write("\n" + "-"*75 + "\n")
        file.write("--- Resumo Final ---\n")
        file.write(f"Raiz encontrada:     {raiz:.8f}\n")
        file.write(f"Erro final estimado: {erro:.2e}\n")
        file.write(f"Numero de iteracoes: {iteracoes}\n")
        file.write(f"Tempo de execucao:   {tempo:.6f} segundos\n")

    def bissecao(self):
        """Executa o método da Bisseção e gera um relatório detalhado."""
        if self.f(self.a) * self.f(self.b) >= 0:
            print("\nAVISO: Não há garantia de raiz no intervalo para o método da Bissecção.")
            return

        a, b = self.a, self.b
        output_filename = os.path.join("output", "bissecao_saida.txt")
        start_time = time.time()
        
        with open(output_filename, "w", encoding='utf-8') as file:
            file.write(f"--- Relatorio do Metodo da Bissecao ---\n")
            file.write(f"Funcao: f(x) = {self.func_str}\n\n")
            file.write(f"{'Iter':>4} | {'a':>12} | {'b':>12} | {'c (raiz)':>12} | {'f(c)':>15} | {'Erro |b-a|':>15}\n")
            file.write("-" * 75 + "\n")

            for k in range(1, 1001):
                c = (a + b) / 2
                f_c = self.f(c)
                error = abs(b - a)
                
                file.write(f"{k:4d} | {a:12.6f} | {b:12.6f} | {c:12.6f} | {f_c:15.6e} | {error:15.6e}\n")

                if error / 2 < self.tolerance or abs(f_c) < 1e-15:
                    tempo = time.time() - start_time
                    self._escrever_resumo(file, c, error / 2, k, tempo)
                    print(f"\nSucesso! Relatório salvo em '{output_filename}'.")
                    return

                if self.f(a) * f_c < 0:
                    b = c
                else:
                    a = c
        print("\nO método não convergiu no número máximo de iterações.")

    def falsa_posicao(self):
        """Executa o método da Posição Falsa e gera um relatório detalhado."""
        if self.f(self.a) * self.f(self.b) >= 0:
            print("\nAVISO: Não há garantia de raiz no intervalo para o método da Posição Falsa.")
            return

        a, b = self.a, self.b
        c_old = float('inf')
        output_filename = os.path.join("output", "posicao_falsa_saida.txt")
        start_time = time.time()

        with open(output_filename, "w", encoding='utf-8') as file:
            file.write(f"--- Relatorio do Metodo da Posicao Falsa ---\n")
            file.write(f"Funcao: f(x) = {self.func_str}\n\n")
            file.write(f"{'Iter':>4} | {'a':>12} | {'b':>12} | {'c (raiz)':>12} | {'f(c)':>15} | {'Erro |c-c_old|':>18}\n")
            file.write("-" * 80 + "\n")

            for k in range(1, 1001):
                f_a, f_b = self.f(a), self.f(b)
                c = (a * f_b - b * f_a) / (f_b - f_a)
                f_c = self.f(c)
                error = abs(c - c_old)

                file.write(f"{k:4d} | {a:12.6f} | {b:12.6f} | {c:12.6f} | {f_c:15.6e} | {error:18.6e}\n")

                if error < self.tolerance or abs(f_c) < 1e-15:
                    tempo = time.time() - start_time
                    self._escrever_resumo(file, c, error, k, tempo)
                    print(f"\nSucesso! Relatório salvo em '{output_filename}'.")
                    return
                
                if f_a * f_c < 0:
                    b = c
                else:
                    a = c
                c_old = c
        print("\nO método não convergiu no número máximo de iterações.")

    def newton_raphson(self):
        """Executa o método de Newton-Raphson e gera um relatório detalhado."""
        x = (self.a + self.b) / 2
        output_filename = os.path.join("output", "newton_raphson_saida.txt")
        start_time = time.time()
        
        with open(output_filename, "w", encoding='utf-8') as file:
            file.write(f"--- Relatorio do Metodo de Newton-Raphson ---\n")
            file.write(f"Funcao: f(x) = {self.func_str}\n")
            file.write(f"Chute inicial: x0 = {x:.6f}\n\n")
            file.write(f"{'Iter':>4} | {'x_i':>15} | {'f(x_i)':>15} | {"f'(x_i)":>15} | {'Erro |x_i-x_i-1|':>20}\n")
            file.write("-" * 78 + "\n")

            for k in range(1, 1001):
                f_x = self.f(x)
                f_prime_x = self.f_prime(x)

                if abs(f_prime_x) < 1e-12:
                    print("\nERRO: Derivada próxima de zero. O método falhou.")
                    file.write("Derivada nula ou muito pequena. Metodo interrompido.\n")
                    return

                x_new = x - f_x / f_prime_x
                error = abs(x_new - x)
                
                file.write(f"{k:4d} | {x:15.8f} | {f_x:15.6e} | {f_prime_x:15.6e} | {error:20.6e}\n")

                if error < self.tolerance or abs(f_x) < 1e-15:
                    tempo = time.time() - start_time
                    self._escrever_resumo(file, x_new, error, k, tempo)
                    print(f"\nSucesso! Relatório salvo em '{output_filename}'.")
                    return
                
                x = x_new
        print("\nO método não convergiu no número máximo de iterações.")

    def secante(self):
        """Executa o método da Secante e gera um relatório detalhado."""
        x0, x1 = self.a, self.b
        output_filename = os.path.join("output", "secante_saida.txt")
        start_time = time.time()

        with open(output_filename, "w", encoding='utf-8') as file:
            file.write(f"--- Relatorio do Metodo da Secante ---\n")
            file.write(f"Funcao: f(x) = {self.func_str}\n")
            file.write(f"Pontos iniciais: x0 = {x0}, x1 = {x1}\n\n")
            file.write(f"{'Iter':>4} | {'x_i+1':>15} | {'f(x_i+1)':>15} | {'Erro |x_i+1 - x_i|':>22}\n")
            file.write("-" * 65 + "\n")

            for k in range(1, 1001):
                f_x0, f_x1 = self.f(x0), self.f(x1)
                
                if abs(f_x1 - f_x0) < 1e-12:
                    print("\nERRO: Divisão por zero evitada. O método da Secante falhou.")
                    file.write("Divisao por valor muito pequeno. Metodo interrompido.\n")
                    return
                
                x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
                error = abs(x2 - x1)
                
                file.write(f"{k:4d} | {x2:15.8f} | {self.f(x2):15.6e} | {error:22.6e}\n")

                if error < self.tolerance or abs(self.f(x2)) < 1e-15:
                    tempo = time.time() - start_time
                    self._escrever_resumo(file, x2, error, k, tempo)
                    print(f"\nSucesso! Relatório salvo em '{output_filename}'.")
                    return
                
                x0, x1 = x1, x2
        print("\nO método não convergiu no número máximo de iterações.")

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
            
            if choice not in [1, 2, 3, 4]:
                print("Opção inválida. Tente novamente.")
                continue

            filename = input("Digite o nome do arquivo de entrada (ex: entrada.txt): ")
            
            os.makedirs("output", exist_ok=True)
            if not os.path.exists("input"):
                print("\nERRO: A pasta 'input' não foi encontrada. Crie a pasta e coloque seu arquivo de entrada lá.")
                continue

            calc = CalculadoraNumerica(filename)

            if choice == 1:
                calc.bissecao()
            elif choice == 2:
                calc.falsa_posicao()
            elif choice == 3:
                calc.newton_raphson()
            elif choice == 4:
                calc.secante()

        except ValueError:
            print("\nEntrada inválida. Por favor, digite um número.")
        except KeyboardInterrupt:
            print("\nOperação cancelada. Saindo.")
            break

if __name__ == "__main__":
    main()

