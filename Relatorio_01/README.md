# 🧮 Calculadora de Análise Numérica

Este é um projeto desenvolvido para a disciplina de Análise Numérica, do
curso de Ciência da Computação na Universidade Estadual de Santa Cruz
(UESC).

O objetivo deste projeto é implementar e analisar diversos métodos
numéricos fundamentais para a resolução de problemas matemáticos,
encapsulando-os numa calculadora interativa em Python. A ferramenta
permite ao utilizador resolver problemas de raízes de funções e sistemas
de equações lineares, além de analisar a condição de matrizes.

## 🎯 Métodos Implementados

A calculadora oferece uma suíte de algoritmos clássicos, divididos em
três módulos principais:

### 1. Raízes de Funções Reais

Métodos para encontrar o valor de x para o qual f(x)=0.

-   **Bissecção**: Garante a convergência de forma segura, ideal para
    garantir um resultado.
-   **Posição Falsa**: Uma otimização da Bissecção, geralmente mais
    rápida.
-   **Newton-Raphson**: Convergência quadrática e muito rápida, mas
    exige a derivada e um bom ponto inicial.
-   **Secante**: Alternativa a Newton quando a derivada não é conhecida,
    mantendo uma velocidade de convergência elevada.

### 2. Sistemas de Equações Lineares

Algoritmos para encontrar o vetor x que satisfaz a equação Ax=b.

-   **Eliminação de Gauss**: Método direto e robusto para obter a
    solução exata.
-   **Fatoração LU**: Eficiente para resolver o mesmo sistema com
    múltiplos vetores b.
-   **Jacobi**: Método iterativo, ideal para sistemas de grande escala e
    esparsos.
-   **Gauss-Seidel**: Uma versão otimizada de Jacobi, com convergência
    tipicamente mais rápida.

### 3. Análise de Matrizes

-   **Condição da Matriz**: Calcula o número de condição de uma matriz
    para avaliar a sua estabilidade numérica.

## 📁 Estrutura de Pastas

    .
    ├── Codigo/
    │   ├── CalculadorDeRaizes/      # Módulo para encontrar raízes
    │   │   ├── __init__.py
    │   │   ├── core.py              # Lógica principal e leitura de ficheiros
    │   │   ├── metodos.py           # Implementação dos algoritmos
    │   │   └── relatorios.py        # Geração dos relatórios de saída
    │   ├── CondicionamentoMatrizes/ # Módulo para análise de matrizes
    │   │   └── ...
    │   ├── SistemasLineares/        # Módulo para sistemas lineares
    │   │   └── ...
    │   ├── Input/                   # Pasta para os ficheiros de entrada
    │   │   └── entrada_exemplo.txt
    │   ├── output/                  # Pasta para os relatórios gerados
    │   │   └── bissecao_saida.txt
    │   ├── main.py                  # Ponto de entrada do programa (menu interativo)
    │   └── requirements.txt         # Dependências do projeto
    └── README.md

## ▶️ Como Compilar e Executar

### ✅ Requisitos

-   Python 3.x instalado
-   Bibliotecas listadas no `requirements.txt` (principalmente sympy e
    numpy)

### 🧪 Passo a passo

1.  Clone o repositório:

    ``` bash
    git clone https://github.com/seu-usuario/Analise_Numerica.git
    cd Analise_Numerica
    ```

2.  Instale as dependências:

    ``` bash
    pip install -r Codigo/requirements.txt
    ```

3.  Prepare o ficheiro de entrada:

    -   Crie um ficheiro de texto dentro da pasta `Codigo/Input/`.
    -   Siga o formato esperado por cada método (descrito no relatório
        do projeto).

4.  Execute o programa:

    ``` bash
    python Codigo/main.py
    ```

5.  Siga as instruções do menu interativo:

    -   Escolha o método que deseja executar.
    -   Quando solicitado, insira o nome do seu ficheiro de entrada (ex:
        entrada_exemplo.txt).

6.  Verifique os resultados:

    -   Os relatórios detalhados para cada execução serão guardados na
        pasta `Codigo/output/`.

## 📝 Observações

O relatório completo do projeto, com a análise detalhada de cada método
e os resultados dos problemas, pode ser encontrado neste [repositório](https://github.com/Gabriel-R-Galdino/Analise_Numerica).

## 🎓 Informações Acadêmicas

-   **Disciplina**: Análise Numérica
-   **Professor**: Gesil Sampaio Amarante II
-   **Instituição**: Universidade Estadual de Santa Cruz (UESC)
-   **Semestre**: 2025.2

## 👨‍💻 Autor

Gabriel Rosa Galdino -
[Gabriel-R-Galdino](https://github.com/Gabriel-R-Galdino)
