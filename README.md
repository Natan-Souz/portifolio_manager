# Controle de portfólio

Este projeto é um gerenciador de carteira de ações que permite aos usuários monitorar seus investimentos, calcular indicadores financeiros e vizualizar desempenho por meio de uma interface gráfica. Ele utiliza a base de dados do Yahoo Finance para obter informações sobre os ativos.


## Funcionalidades

- Adicionar e remover ações na carteira
- Monitorar preços e calcular lucro/prejuízo
- Calcular indicadores financeiros disponíveis no Yahoo Finance ou derivados de seus dados:
- ROI (Retorno sobre Investimento)
- P/VPA (Preço sobre Valor Patrimonial)
- Dividend Yield
- LPA (Lucro por Ação)
- P/L (Preço/Lucro)
- Volatilidade histórica (calculada a partir dos preços históricos)
- Exibir gráficos interativos e relatórios
- Atualização automática dos dados

## Tecnologias utilizadas 
Python 3.x

- yfinance (obtenção de dados financeiros)
- pandas (manipulação de dados)
- matplotlib e plotly (visualização de gráficos)
- SQLite e SQLAlchemy (armazenamento de dados)
- Dash

## Como Executar o Projeto

### 1. Clone o repositório

```bash
  git clone https://github.com/seu-usuario/gerenciador-carteira-acoes.git
```

### 2. Entre no diretório do projeto

```bash
  cd gerenciador-carteira-acoes
```

### 3. Crie e ative o ambiente virtual

```bash
  python -m venv .venv
  .venv\Scripts\activate
```

### 4. Instale as dependências

```bash
  pip install -r requirements.txt
```

### 5. Execute o projeto

```bash
  python main.py    
```