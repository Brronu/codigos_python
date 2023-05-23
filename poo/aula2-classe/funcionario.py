
class Funcionario:
    #Criando metodo construtor
    def __init__(self, nome, cargo, salario):
        #estamos criando os atributos da classe utilizando metodo construtor. nesse caso precisamos passar os parãmetro que serão usados como valores dos atributos da classe.
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def exibirDados(self):
        print(f"Ola {self.nome} seu cargo e {self.cargo} seu salario e {self.salario}")
