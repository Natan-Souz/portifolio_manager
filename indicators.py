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

def calcular_pl(ticker):
    """
    Calcula os Preço / Lucro (PL)
    Formula: Preço Atual / Lucro por Ação
    Obtido diretamente do Yahoo Finance
    """
    preco_atual = obter_preco_atual(ticker)
    dados = obter_dados_fundamentais(ticker)
    lpa = dados.get("LPA (Lucro por Ação)")

    if not lpa or lpa == 0:
        return None
    
    return round(preco_atual/lpa, 2)

def calcular_volatilidade(ticker, periodo="1y"):
    """
    Calcula A volatilidade histórica do ativo (Volatilidade Histórica)
    Formula: Necessário calcular o desvio padrão dos retornos diarios
    """
    historico = session.query(HistoricoPrecos).filter_by(ticker=ticker).all()
    if not historico:
        return None

    precos = [h.preco_fechamento for h in historico]
    retornos = np.diff(precos) / precos[:-1]
    volatilidade = np.std(retornos) * np.sqrt(252)  # Ajuste para escala anual
    return round(volatilidade, 4)

def calcular_sharpe(ticker, taxa_livre_risco=0.03):
    """ 
    Calcula o Indice Sharpe
    Formula: (Retorno Esperado - Taxa Livre de Risco) / Volatilidade
    """
    retorno_medio = session.query(HistoricoPrecos).filter_by(ticker=ticker).all()
    if not retorno_medio:
        return None

    retorno_medio = np.mean([h.preco_fechamento for h in retorno_medio])
    volatilidade = calcular_volatilidade(ticker)

    if not volatilidade or volatilidade == 0:
        return None

    sharpe = (retorno_medio - taxa_livre_risco) / volatilidade
    return round(sharpe, 4)


def salvar_indicadores_no_banco(ticker):
    """
    Calcula e salva os indicadores financeiros no banco de dados 
    """
    indicadores = Indicadores(
        ticker=ticker,
        roi=calcular_roi(ticker),
        pvpa=calcular_pvpa(ticker),
        dividend_yield=calcular_dividend_yield(ticker),
        pl=calcular_pl(ticker),
        volatilidade=calcular_volatilidade(ticker),
        sharpe=calcular_sharpe(ticker)
    )

    session.add(indicadores)
    session.commit()