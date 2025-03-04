import numpy as np
import pandas as pd
from database import session, Indicadores, HistoricoPrecos
from data_handler import obter_preco_atual, obter_dados_fundamentais

def calcular_roi(ticker):
    """
    Calcula o retorno sobre investimento (ROI)
    Formula: (Lucro Total/Investimento Total) X 100
    """
    preco_atual = obter_preco_atual(ticker)
    transacoes = session.query(Indicadores).filter_by(ticker=ticker).all()

    if not transacoes:
        return None
    
    #Custo total da compra
    total_custo = sum(t.lpa * t.vpa for t in transacoes if t.lpa and t.vpa)
    if total_custo == 0:
        return None
    
    #Calculo do lucro
    lucro_total = (preco_atual * len(transacoes)) - total_custo
    roi = (lucro_total/total_custo) * 100
    return round(roi, 2)

def calcular_pvpa(ticker):
    """ 
    Calcula o Preço sobre Valor Patrimonial (P/VPA)
    Formula: Preço Atual / Valor Patrimonial
    """
    preco_atual = obter_preco_atual(ticker)
    dados = obter_dados_fundamentais(ticker)
    vpa = dados.get("VPA (Valor Patrimonial por Ação)")

    if not vpa or vpa == 0:
        return None
    
    return round(preco_atual/ vpa, 2)

def calcular_dividend_yield(ticker):
    """
    Calcula os ganhos de dividendos
    Formula: Dividendos Anuais / Preço Atual * 100
    Obtido diretamente do Yahoo Finance
    """
    dados = obter_dados_fundamentais(ticker)
    dividend_yield = dados.get("Dividend Yield")

    return round (dividend_yield, 4) if dividend_yield else None