from database import Base, engine

print("Criando tabelas no banco de dados...")
Base.metadata.create_all(engine)
print("Banco de dados pronto!")