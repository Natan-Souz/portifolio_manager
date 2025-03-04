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