import os
import sys

from EquacoesDiferenciais.core import CalculadorEDO

def main():
    while True:
        print("\n======= Calculadora EDO (Equações Diferenciais) =======")
        print("--- Problemas de Valor Inicial (PVI) ---")
        print("1. Método de Euler Simples")
        print("2. Método de Heun")
        print("3. Método de Euler Modificado")
        print("4. Método de Ralston")
        print("5. Runge-Kutta 3ª Ordem")
        print("6. Runge-Kutta 4ª Ordem")
        print("\n--- Problemas de Valor de Contorno (PVC) ---")
        print("7. Método do Shooting (Tiro)")
        print("8. Diferenças Finitas")
        print("\n--- Gerar Gráficos ---")
        print("9. Gerar Gráfico Comparativo de Tempo")
        print("\n0. Sair")
        
        try:
            choice = int(input("\nEscolha uma opção: "))
            
            if choice == 0:
                print("Encerrando execução.")
                break

            # Verificações de ambiente
            os.makedirs("output", exist_ok=True)
            if not os.path.exists("input"):
                print("\nERRO: A pasta 'input' não foi encontrada. Crie-a e coloque os arquivos de entrada nela.")
                continue

            # Validação básica de intervalo de opção
            if choice not in range(1, 9):
                print("Opção inválida. Tente novamente.")
                continue

            filename = input("Digite o nome do arquivo de entrada (ex: entrada_edo.txt): ")

            # Lógica de Instanciação baseada no tipo de problema (PVI ou PVC)
            if 1 <= choice <= 6:
                # Instancia para PVI
                calc = CalculadorEDO(filename, tipo_problema="PVI")
                
                if choice == 1:
                    calc.run_euler()
                elif choice == 2:
                    calc.run_heun()
                elif choice == 3:
                    calc.run_euler_modificado()
                elif choice == 4:
                    calc.run_ralston()
                elif choice == 5:
                    calc.run_rk3()
                elif choice == 6:
                    calc.run_rk4()

            elif 7 <= choice <= 8:
                # Instancia para PVC
                calc = CalculadorEDO(filename, tipo_problema="PVC")
                
                if choice == 7:
                    calc.run_shooting()
                elif choice == 8:
                    calc.run_finite_differences()
            
            elif choice == 9:
                print("\nQual tipo de problema deseja comparar?")
                print("1. PVI (Problema de Valor Inicial)")
                print("2. PVC (Problema de Valor de Contorno)")
                
                try:
                    sub_choice = int(input("Escolha (1 ou 2): "))
                    
                    if sub_choice == 1:
                        tipo = "PVI"
                    elif sub_choice == 2:
                        tipo = "PVC"
                    else:
                        print("Opção inválida. Retornando ao menu.")
                        continue

                    # Instancia e roda o comparativo
                    calc = CalculadorEDO(filename, tipo_problema=tipo)
                    calc.run_comparativo()

                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")

        except ValueError:
            print("\nEntrada inválida. Por favor, digite um número.")
        except KeyboardInterrupt:
            print("\nOperação cancelada pelo usuário. Saindo.")
            break
        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()