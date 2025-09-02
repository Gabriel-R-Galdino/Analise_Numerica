import os
from calculadora_numerica.core import CalculadoraNumerica

def main():
    """Exibe o menu"""
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
                print("\nERRO: A pasta 'input' não foi encontrada.")
                continue

            calc = CalculadoraNumerica(filename)

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
        except KeyboardInterrupt:
            print("\nOperação cancelada. Saindo.")
            break

if __name__ == "__main__":
    main()