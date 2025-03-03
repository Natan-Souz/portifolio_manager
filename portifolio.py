from datetime import datetime
from data_handler import obter_preco_atual

class Portfolio:
    def __init__(self):
        # Inicializa o portfólio carregando todas as transações do banco de dados
        self.transacoes = [] #lista temporária

    def carregar_transacoes(self):
        #implementação posterior
        pass    

    def adicionar_transacoes(self, ticker, quantidade, preco, data, tipo):
        transacao = {
            "ticker": ticker,
            "quantidade": quantidade,
            "preco": preco,
            "data": data,
            "tipo": tipo,
        }
        self.transacoes.append(transacao)

    def calcular_lucro_prejuizo(self,ticker):
        #implementação posterior
        pass

    def obter_posicao(self):
        posicao = {}
        for transacao in self.transacoes:
            ticker = transacao["ticker"]
            if ticker not in posicao:
                posicao[ticker] = 0
            posicao[ticker] += transacao["quantidade"] if transacao["tipo"] == "compra" else - transacao["quantidade"]
        return posicao