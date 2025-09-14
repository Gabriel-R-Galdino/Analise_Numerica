import os
from CalculadorDeRaizes.core import CalculadorDeRaizes
from SistemasLineares.core import CalculadorDeSistemas
from CondicionamentoMatrizes.core import CalculadorDeCondicao

def menu_raizes():
    print("\n--- Calcular Raízes de Funções ---")
    print("1. Bissecção")
    print("2. Posição Falsa")
    print("3. Newton-Raphson")
    print("4. Secante")
    
    try:
        choice = int(input("Escolha um método: "))
        if choice not in [1, 2, 3, 4]:
            print("Opção inválida. Tente novamente.")
            return

        filename = input("Digite o nome do arquivo de entrada (ex: entrada_raizes.txt): ")
        calc = CalculadorDeRaizes(filename)

        if choice == 1:
            calc.run_bissecao()
        elif choice == 2:
            calc.run_falsa_posicao()
        elif choice == 3:
            calc.run_newton_raphson()
        elif choice == 4:
            calc.run_secante()

    except ValueError:
        print("\nEntrada inválida. Por favor, digite um número.")

def menu_sistemas_lineares():
    print("\n--- Resolver Sistemas Lineares ---")
    print("1. Eliminação de Gauss")
    print("2. Fatoração LU")
    print("3. Jacobi")
    print("4. Gauss-Seidel")

    try:
        choice = int(input("Escolha um método: "))
        if choice not in [1, 2, 3, 4]:
            print("Opção inválida. Tente novamente.")
            return

        filename = input("Digite o nome do arquivo de entrada (ex: entrada_sistemas.txt): ")
        calc = CalculadorDeSistemas(filename)

        if choice == 1:
            calc.run_gauss()
        elif choice == 2:
            calc.run_lu()
        elif choice == 3:
            calc.run_jacobi()
        elif choice == 4:
            calc.run_gauss_seidel()

    except ValueError:
        print("\nEntrada inválida. Por favor, digite um número.")

def menu_condicionamento():
    try:
        filename = input("\nDigite o nome do arquivo de entrada da matriz (ex: entrada_matriz.txt): ")
        calc = CalculadorDeCondicao(filename)
        calc.run_condicionamento()
    except ValueError:
        print("\nEntrada inválida.")

def main():
    while True:
        print("\n======= Calculadora de Métodos Numéricos =======")
        print("1. Calcular Raízes de Funções")
        print("2. Resolver Sistemas Lineares")
        print("3. Analisar Condicionamento de Matrizes")
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
                menu_raizes()
            elif choice == 2:
                menu_sistemas_lineares()
            elif choice == 3:
                menu_condicionamento()
            else:
                print("Opção inválida. Tente novamente.")

        except ValueError:
            print("\nEntrada inválida. Por favor, digite um número.")
        except KeyboardInterrupt:
            print("\nOperação cancelada. Saindo.")
            break

if __name__ == "__main__":
    main()