from datetime import datetime
from database import session, Transacao
from data_handler import obter_preco_atual

class Portfolio:
    def __init__(self):
        # Inicializa o portfólio carregando todas as transações do banco de dados
        self.transacoes = session.query(Transacao).all()

    def adicionar_transacoes(self, ticker, quantidade, preco, data, tipo):
        transacao = Transacao(
            ticker = ticker,
            quantidade = quantidade,
            preco = preco,
            data = datetime.strptime(data, '%Y-%m-%d'),
            tipo = tipo
        )
        session.add(transacao)
        session.commit()
        self.transacoes.append(transacao)

    def obter_posicao(self):
        posicao = {}

        for transacao in self.transacoes:
            ticker = transacao.ticker
            if ticker not in posicao:
                posicao[ticker] = 0
            posicao[ticker] += transacao.quantidade if transacao.tipo == 'compra' else -transacao.quantidade
        return posicao
    
    def calcular_lucro_prejuizo(self, ticker):
        transacoes = [t for t in self.transacoes if t.ticker == ticker]

        if not transacoes:
            return {"Erro": "Nenhuma transação encontrada para esse ativo"}
    
        #Separar compras e vendas
        compras = [t for t in transacoes if t.tipo == "compra"]
        vendas = [t for t in transacoes if t.tipo == "venda"]

        #Preço médio
        total_custo = sum(t.preco * t.quantidade for t in compras)
        total_acoes_compradas = sum(t.quantidade for t in compras)
        preco_medio = total_custo / total_acoes_compradas if total_acoes_compradas > 0 else 0

        #Preço do ativo
        preco_atual = obter_preco_atual(ticker)

        #Lucro / Prejuizo
        total_vendas = sum(t.preco * t.quantidade for t in vendas)
        quantidade_vendida = sum(t.quantidade for t in vendas)
        lucro_vendas  = total_vendas - (preco_medio * quantidade_vendida)

        #calculo de valorização das ações
        quantidade_restante = total_acoes_compradas - quantidade_vendida
        lucro_atual= (preco_atual - preco_medio) * quantidade_restante if quantidade_restante > 0 else 0

        # Lucro/prejuízo total = Lucro das vendas + valorização das ações mantidas
        lucro_total = lucro_vendas + lucro_atual

        return {
            "Preço Médio": round(preco_medio, 2),
            "Preço Atual": round(preco_atual, 2),
            "Lucro/Prejuízo Total": round(lucro_total, 2),
            "Lucro em Vendas": round(lucro_vendas, 2),
            "Valorização Atual": round(lucro_atual, 2)
        }