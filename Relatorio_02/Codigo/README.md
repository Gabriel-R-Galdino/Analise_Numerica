# 🧮 Calculadora de Análise Numérica (Relatório 02)

Este é um projeto desenvolvido para a disciplina de Análise Numérica, do
curso de Ciência da Computação na Universidade Estadual de Santa Cruz (UESC).

Este projeto expande a calculadora numérica com módulos focados em aproximação de funções, interpolação, derivação e integração numérica. A ferramenta mantém a estrutura modular em Python, permitindo ao utilizador resolver novos conjuntos de problemas complexos.

## 🎯 Métodos Implementados

A calculadora foi expandida com os seguintes módulos:

### 1. Aproximação de Funções e Regressão

Métodos para encontrar a curva que melhor se ajusta a um conjunto de dados ou a uma função contínua.
- **Regressão Linear**: Encontra a reta ($y = ax + b$) que minimiza o erro quadrático para um conjunto de pontos.
- **Aproximação Polinomial (Caso Discreto)**: Encontra um polinômio de grau $N$ que melhor se ajusta a um conjunto de pontos.
- **Aproximação Polinomial (Caso Contínuo)**: Encontra um polinômio que melhor aproxima uma função contínua $f(x)$ dentro de um intervalo.

### 2. Interpolação Polinomial

Algoritmos para encontrar um polinômio que passa _exatamente_ por um conjunto de pontos.
- **Polinômios de Lagrange**: Método direto para construir o polinômio interpolador.
- **Diferenças Divididas de Newton**: Método incremental e computacionalmente eficiente para construir o polinômio.

### 3. Derivação Numérica

Técnicas para estimar a derivada de uma função em um ponto específico.
- **Diferenças Finitas (1ª Ordem)**: Estima a **primeira derivada** em um ponto usando a fórmula de diferença central.
- **Diferenças Finitas (2ª Ordem)**: Estima a **segunda derivada** em um ponto.

### 4. Integração Numérica

Métodos para calcular a integral definida de uma função (a área sob a curva).
- **Regra dos Trapézios (Simples e Múltipla)**: Aproxima a área sob a curva dividindo-a em trapézios.
- **Regra 1/3 de Simpson (Simples e Múltipla)**: Aproximação mais precisa que utiliza parábolas para modelar a curva.
- **Regra 3/8 de Simpson (Simples e Múltipla)**: Alternativa para quando o número de intervalos é múltiplo de 3.
- **Extrapolação de Richards**: Técnica para melhorar a precisão de outros métodos de integração, combinando estimativas de diferentes tamanhos de passo.
- **Quadratura de Gauss-Legendre**: Método de alta precisão que avalia a função em pontos não igualmente espaçados (pontos de Gauss) para otimizar o resultado.

## 📁 Estrutura de Pastas

O projeto segue a mesma arquitetura modular do primeiro relatório:
```
    .
    ├── Codigo/
    │ ├── AproximacaoRegressao/ # Módulo de Aproximação e Regressão
    │ │ ├── init.py
    │ │ ├── core.py             # Lógica principal e leitura de ficheiros
    │ │ ├── metodos.py          # Implementação dos algoritmos
    │ │ └── relatorios.py       # Geração dos relatórios de saída
    │ ├── DerivacaoNumerica/    # Módulo de Derivação
    │ │ ├── init.py
    │ │ ├── core.py             # Lógica principal e leitura de ficheiros
    │ │ ├── metodos.py          # Implementação dos algoritmos
    │ │ └── relatorios.py       # Geração dos relatórios de saída
    │ ├── IntegracaoNumerica/   # Módulo de Integração
    │ │ ├── init.py
    │ │ ├── core.py             # Lógica principal e leitura de ficheiros
    │ │ ├── metodos.py          # Implementação dos algoritmos
    │ │ └── relatorios.py       # Geração dos relatórios de saída
    │ ├── Interpolacao/         # Módulo de Interpolação
    │ │ ├── init.py
    │ │ ├── core.py             # Lógica principal e leitura de ficheiros
    │ │ ├── metodos.py          # Implementação dos algoritmos
    │ │ └── relatorios.py       # Geração dos relatórios de saída
    │ ├── Input/                # Pasta para os ficheiros de entrada
    │ │ ├── entrada_aprox_regr.txt
    │ │ └── ...
    │ ├── output/               # Pasta para os relatórios gerados
    │ │ └── ...
    │ ├── main.py               # Ponto de entrada (menu interativo)
    │ └── requirements.txt      # Dependências do projeto
    └── README.md               # Este ficheiro
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
    cd Analise_Numerica/Relatorio_02
    ```

3.  Instale as dependências:

    ```bash
    pip install -r Codigo/requirements.txt
    ```

4.  Prepare o ficheiro de entrada:

    - Crie um ficheiro de texto dentro da pasta `Codigo/Input/`.
    - Siga o formato esperado por cada método (ex: `funcao;a,b;n` para integração).

5.  Execute o programa:

    ```bash
    python Codigo/main.py
    ```

6.  Siga as instruções do menu interativo:

    - Escolha o módulo (ex: 4. Integração Numérica).
    - Escolha o método (ex: 2. Trapézios Múltiplos).
    - Quando solicitado, insira o nome do seu ficheiro de entrada (ex: `entrada_integ.txt`).

7.  Verifique os resultados:
    - Os relatórios detalhados para cada execução serão guardados na pasta `Codigo/output/`.

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
