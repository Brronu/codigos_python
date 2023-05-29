import pymysql 

# Estabelecendo a conexão
conexao = pymysql.connect(
    host= "localhost",
    user="root",
    password="",
    database="departamento_bd"
)

# Inserindo dados no banco
codigo = int(input("Informe o codigo do funcionario: "))
nome = input("Infome o nome do funcionario: ")
salario = float(input("Informe o salario do funcionario: "))
cargo = input("Informe o cargo do funcionario: ")
  
# Colocamos %s no lugar dos dados reais, para evitar possiveis ataques sql injection. Isso e uma implementação da biblioteca pymysql
comando = "insert into funcionario values(%s, %s, %s, %s)"

campos = (codigo, nome, salario, cargo)# Criando uma tupla com os dados que serão substituidos no comando

consulta = conexao.cursor() # Cursor() e o objeto que ira interagir diretamente com bancos de dados

consulta.execute(comando,campos,)

conexao.commit() # gravaros dados no banco

print(consulta.rowcount, "linha(s) inserinda com sucesso\n")

conexao.close()
