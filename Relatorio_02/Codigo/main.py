import os
import sys

from AproximacaoRegressao.core import CalculadorAproximacao
from Interpolacao.core import CalculadorInterpolacao
from DerivacaoNumerica.core import CalculadorDerivacao
from IntegracaoNumerica.core import CalculadorIntegracao

def menu_aproximacao_regressao():
    print("\n--- Aproximação e Regressão ---")
    print("1. Regressão Linear")
    print("2. Aproximação Polinomial (Discreto)")
    print("3. Aproximação Polinomial (Contínuo)")

    try:
        choice = int(input("Escolha um método: "))
        filename = input("Digite o nome do arquivo de entrada (ex: entrada_aprox.txt): ")

        if choice == 1:
            # Tipo "discreto" para ler pares (x,y)
            calc = CalculadorAproximacao(filename, "discreto")
            calc.run_linear_regression()
        elif choice == 2:
            # Tipo "discreto" para ler pares (x,y)
            calc = CalculadorAproximacao(filename, "discreto")
            calc.run_discrete_polynomial()
        elif choice == 3:
            # Tipo "continuo" para ler f(x) e intervalo
            calc = CalculadorAproximacao(filename, "continuo")
            calc.run_continuous_polynomial()
        else:
            print("Opção inválida.")

    except (ValueError, TypeError):
        print("\nEntrada inválida. Tente novamente.")
    except FileNotFoundError:
        print(f"\nERRO: Arquivo '{filename}' não encontrado na pasta 'input'.")

def menu_interpolacao():
    print("\n--- Interpolação Polinomial ---")
    print("1. Polinômios de Lagrange")
    print("2. Diferenças Divididas de Newton")
    
    try:
        choice = int(input("Escolha um método: "))
        filename = input("Digite o nome do arquivo de entrada (ex: entrada_interp.txt): ")
        
        calc = CalculadorInterpolacao(filename)

        if choice == 1:
            calc.run_lagrange()
        elif choice == 2:
            calc.run_newton()
        else:
            print("Opção inválida.")
            
    except (ValueError, TypeError):
        print("\nEntrada inválida. Tente novamente.")
    except FileNotFoundError:
        print(f"\nERRO: Arquivo '{filename}' não encontrado na pasta 'input'.")

def menu_derivacao():
    print("\n--- Derivação Numérica ---")
    print("1. 1ª Ordem (Diferenças Finitas)")
    print("2. 2ª Ordem (Diferenças Finitas)")
    
    try:
        choice = int(input("Escolha um método: "))
        filename = input("Digite o nome do arquivo de entrada (ex: entrada_deriv.txt): ")
        
        calc = CalculadorDerivacao(filename)

        if choice == 1:
            calc.run_first_order()
        elif choice == 2:
            calc.run_second_order()
        else:
            print("Opção inválida.")

    except (ValueError, TypeError):
        print("\nEntrada inválida. Tente novamente.")
    except FileNotFoundError:
        print(f"\nERRO: Arquivo '{filename}' não encontrado na pasta 'input'.")

def menu_integracao():
    print("\n--- Integração Numérica ---")
    print("1. Trapézios Simples")
    print("2. Trapézios Múltiplos")
    print("3. Simpson 1/3 Simples")
    print("4. Simpson 1/3 Múltiplos")
    print("5. Simpson 3/8 Simples")
    print("6. Simpson 3/8 Múltiplos")
    print("7. Extrapolação de Richards")
    print("8. Quadratura de Gauss")

    try:
        choice = int(input("Escolha um método: "))
        if choice not in range(1, 9):
            print("Opção inválida.")
            return

        filename = input("Digite o nome do arquivo de entrada (ex: entrada_integ.txt): ")
        calc = CalculadorIntegracao(filename)

        if choice == 1:
            calc.run_trapezoidal_simples()
        elif choice == 2:
            calc.run_trapezoidal_multiplos()
        elif choice == 3:
            calc.run_simpson_1_3_simples()
        elif choice == 4:
            calc.run_simpson_1_3_multiplos()
        elif choice == 5:
            calc.run_simpson_3_8_simples()
        elif choice == 6:
            calc.run_simpson_3_8_multiplos()
        elif choice == 7:
            calc.run_richards()
        elif choice == 8:
            calc.run_gaussian_quadrature()

    except (ValueError, TypeError):
        print("\nEntrada inválida. Tente novamente.")
    except FileNotFoundError:
        print(f"\nERRO: Arquivo '{filename}' não encontrado na pasta 'input'.")


def main():
    while True:
        print("\n======= Calculadora de Métodos Numéricos (Relatório 02) =======")
        print("1. Aproximação e Regressão")
        print("2. Interpolação Polinomial")
        print("3. Derivação Numérica")
        print("4. Integração Numérica")
        print("0. Sair")
        
        try:
            choice = int(input("Escolha uma opção: "))
            
            os.makedirs("output", exist_ok=True)
            if not os.path.exists("input"):
                print("\nERRO: A pasta 'input' não foi encontrada. Crie-a e coloque os arquivos de entrada nela.")
                continue

            if choice == 0:
                print("Saindo do programa.")
                break
            elif choice == 1:
                menu_aproximacao_regressao()
            elif choice == 2:
                menu_interpolacao()
            elif choice == 3:
                menu_derivacao()
            elif choice == 4:
                menu_integracao()
            else:
                print("Opção inválida. Tente novamente.")

        except ValueError:
            print("\nEntrada inválida. Por favor, digite um número.")
        except KeyboardInterrupt:
            print("\nOperação cancelada. Saindo.")
            break
        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e}")
            break

if __name__ == "__main__":
    main()