from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

class Base(DeclarativeBase):
    pass

#conexão com SQLite
engine = create_engine('sqlite:///portfolio.db')

#Tabela de transações
class Transacao(Base):
    __tablename__ = 'transacoes'
    id = Column(Integer, primary_key=True)
    ticker = Column(String)
    quantidade = Column(Integer)
    preco = Column(Float)
    data = Column(Date)
    tipo = Column(String) #Compra ou venda

class HistoricoPrecos(Base):
    __tablename__ = 'historico_precos'
    id = Column(Integer, primary_key=True)
    ticker = Column(String, index=True)
    data = Column(Date)
    preco_abertura = Column(Float)
    preco_fechamento = Column(Float)
    maximo = Column(Float)
    minimo = Column(Float)
    volume = Column(Float)
    
class Indicadores(Base):
    __tablename__ = 'indicadores'
    id = Column(Integer, primary_key=True)
    ticker = Column(String, index=True)
    data = Column(Date)
    lpa = Column(Float)
    vpa = Column(Float)
    dividend_yield = Column(Float)
    pl = Column(Float)
    forward_dividend_yield = Column(Float)

# Cria as tabelas no banco de dados
Base.metadata.create_all(engine)

#sessão de interação com o db
Session = sessionmaker(bind=engine)
session = Session()