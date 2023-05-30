import os
os.system("cls")
import pymysql

conexao = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="departamento_bd"
)

comando = "select * from funcionario"

consulta = conexao.cursor()

consulta.execute(comando)

#Exibir a consulta do banco
resultado = consulta.fetchall()# fetchall ira trazer todas as linhas da registro que existem no banco

print(resultado,"\n")

for itens in resultado:
    print(f"Nome: {itens[1]}, Cargo: {itens[3]}")

print("\n")

conexao.close()
