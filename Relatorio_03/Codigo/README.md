# 🧮 Calculadora de Análise Numérica (Relatório 03)

Este é um projeto desenvolvido para a disciplina de Análise Numérica, do
curso de Ciência da Computação na Universidade Estadual de Santa Cruz (UESC).

Este projeto foca na resolução numérica de **Equações Diferenciais Ordinárias**, abordando tanto Problemas de Valor Inicial (PVI) quanto Problemas de Valor de Contorno (PVC). A ferramenta utiliza uma arquitetura modular em Python, permitindo a fácil extensão e manutenção dos métodos implementados.

## 🎯 Métodos Implementados

A calculadora inclui algoritmos clássicos e robustos para a resolução de EDOs:

### 1. Problemas de Valor Inicial (PVI)

Métodos iterativos que partem de um ponto conhecido $(x_0, y_0)$ para estimar os pontos subsequentes da função.

- **Método de Euler Simples**: O método mais básico, utiliza a tangente no ponto inicial para estimar o próximo passo.
- **Método de Heun**: Também conhecido como Euler Aprimorado (Preditor-Corretor), refina a estimativa usando a média das inclinações.
- **Método de Euler Modificado**: Utiliza a inclinação no ponto médio do intervalo para projetar o próximo valor.
- **Método de Ralston**: Um método de Runge-Kutta de 2ª ordem que minimiza o limite do erro de truncamento.
- **Runge-Kutta de 3ª Ordem**: Oferece um equilíbrio entre precisão e custo computacional.
- **Runge-Kutta de 4ª Ordem (RK4)**: O padrão da indústria para resolução de EDOs, oferecendo alta precisão com quatro avaliações de função por passo.

### 2. Problemas de Valor de Contorno (PVC)

Métodos para encontrar a solução de uma EDO que deve satisfazer condições em dois pontos extremos do intervalo (fronteiras).

- **Método do Shooting (Tiro)**: Transforma o problema de contorno em um problema de valor inicial, "chutando" derivadas iniciais até atingir o alvo final.
- **Diferenças Finitas**: Discretiza o domínio e transforma a equação diferencial num sistema de equações lineares, resolvendo todos os pontos simultaneamente.

### 3. Análise de Desempenho

Ferramenta visual para comparação de eficiência computacional.
- **Gráfico Comparativo**: Gera automaticamente um gráfico de barras comparando o tempo de execução de todos os métodos disponíveis (seja para PVI ou PVC) para um mesmo conjunto de problemas, permitindo visualizar o custo-benefício de cada algoritmo.

## 📁 Estrutura de Pastas

O projeto segue uma arquitetura modular organizada por responsabilidade:

```
.
├── EquacoesDiferenciais/       # Módulo Principal de EDO
│   ├── __init__.py
│   ├── core.py                 # Orquestrador: Leitura de arquivos e controle de fluxo
│   ├── metodos.py              # Núcleo Matemático: Implementação pura dos algoritmos
│   ├── graficos.py             # Visualização: Geração de gráficos comparativos com Matplotlib
│   └── relatorios.py           # Camada de Apresentação: Geração de arquivos de saída
├── input/                      # Pasta para os arquivos de entrada
│   ├── entrada_edo.txt
│   └── ...
├── output/                     # Pasta onde os relatórios são salvos
│   └── ...
├── main.py                 # Ponto de entrada exclusivo para este módulo
└── requirements.txt            # Dependências do projeto (SymPy, NumPy)
```

## ▶️ Como Compilar e Executar

### ✅ Requisitos

- Python 3.x instalado
- Bibliotecas listadas no `Codigo/requirements.txt` (principalmente `sympy` e `numpy`)

### 🧪 Passo a passo

1.  Clone o repositório (caso ainda não o tenha):

    ```bash
    git clone [https://github.com/Gabriel-R-Galdino/Analise_Numerica.git](https://github.com/Gabriel-R-Galdino/Analise_Numerica.git)

    ```

2.  Navegue até a pasta deste relatório:

    ```bash
    cd Analise_Numerica/Relatorio_03
    ```

3.  Instale as dependências:

    ```bash
    pip install -r Codigo/requirements.txt
    ```

4.  Prepare o ficheiro de entrada:

    - Crie um arquivo de texto dentro da pasta `input/` (ex: `entrada_edo.txt`).
    - Siga o formato esperado (Exemplo PVI: `funcao; y0; inicio,fim; h`).

5.  Execute o programa:

    ```bash
    python Codigo/main.py
    ```

6.  Siga as instruções do menu interativo:

    - Escolha se deseja resolver um **PVI** (opções 1-6) ou um **PVC** (opções 7-8) ou gerar um Comparativo de Desempenho (opção 9).
    - Digite o nome do arquivo de entrada quando solicitado.

7.  Verifique os resultados:
    - Os relatórios detalhados para cada execução e os gráficos comparativos (.png) serão guardados na pasta `Codigo/output/`.

## 📝 Observações

O relatório completo do projeto, com a análise detalhada de cada método
e os resultados dos problemas, pode ser encontrado neste [repositório](https://github.com/Gabriel-R-Galdino/Analise_Numerica).

## 🎓 Informações Acadêmicas

- **Disciplina**: Análise Numérica
- **Professor**: Gesil Sampaio Amarante II
- **Instituição**: Universidade Estadual de Santa Cruz (UESC)
- **Semestre**: 2025.2

## 👨‍💻 Autor

Gabriel Rosa Galdino - [Gabriel-R-Galdino](https://github.com/Gabriel-R-Galdino)
