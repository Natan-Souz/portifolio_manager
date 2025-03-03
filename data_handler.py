import yfinance as yf
import pandas as pd

def obter_preco_atual(ticker):
    acao = yf.Ticker(ticker)
    info = acao.info
    preco_atual = info.get("regularMarketPrice", "Preços não disponíveis")

    return preco_atual

def obter_historico_preco(ticker, period="1y", intervalo="1d"):
    acao = yf.Ticker(ticker)
    historico = acao.history(period = period, interval = intervalo)
    
    return historico

def obter_dados_fundamentais(ticker):
    acao = yf.Ticker(ticker)
    info = acao.info

    dados = {
        "LPA (Lucro por Ação)": info.get("trailingEps"),
        "VPA (Valor Patrimonial por Ação)": info.get("bookValue"),
        "Dividend Yield (%)": info.get("dividendYield") if info.get("dividendYield") else None,
        "P/L (Preço/Lucro)": info.get("trailingPE"),
    }

    return dados