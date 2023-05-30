import pymysql
class Funcionario:

    def conexao(self):
        conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="departamento_bd"
        )
        return conn
        

    def inserir(self, codigo, nome, salario, cargo):
        conexao = self.conexao() #estamos chamando o metodo que ira connectar ao banco

        comando = "insert into funcionario values(%s, %s, %s, %s)"
        valores = (codigo, nome, salario, cargo)
        consulta = conexao.cursor()
        consulta.execute(comando, valores)
        conexao.commit()
        print(consulta.rowcount,"linha inserindo com sucesso\n")
        conexao.close()

    def consultar(self):
        conexao = self.conexao()

        comando = "select * from funcionario"
        consulta = conexao.cursor()
        consulta.execute(comando)

        resultado = consulta.fetchall()
        print(resultado, "\n")

        conexao.close()
