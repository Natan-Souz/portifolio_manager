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