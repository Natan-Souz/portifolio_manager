from datetime import datetime
from data_handler import obter_preco_atual

class Portfolio:
    def __init__(self):
        # Inicializa o portfólio carregando todas as transações do banco de dados
        self.transacoes = []

    def carregar_transacoes(self):
        #implementação posterior
        pass

    def adicionar_transacoes(self, ticker, quantidade, preco, data, tipo):
        #implementação posterior
        pass

    def calcular_lucro_prejuizo(self,ticker):
        #implementação posterior
        pass

    def obter_posicao(self):
        #implementação posterior
        pass