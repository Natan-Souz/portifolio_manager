from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

#conexão com SQLite
engine = create_engine('sqlite:///portfolio.db')
Base = DeclarativeBase()

#Tabela de transações
class Transacao(Base):
    __tablename__ = 'transacoes'
    id = Column(Integer, primary_key=True)
    ticker = Column(String)
    quantidade = Column(Integer)
    preco = Column(Float)
    data = Column(Date)
    tipo = Column(String) #Compra ou venda

# Cria as tabelas no banco de dados
Base.metadata.create_all(*engine)

#sessão de interação com o db
Session = sessionmaker(bind=engine)
session = Session()