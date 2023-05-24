class Funcionario:
    def __init__(self, cargo, nome):
        self._cargo = cargo
        self._nome = nome
    
    def informacoes(self):
        print(F"Ola {self._nome} seu cargo atual e {self._cargo}\n")

    
class Gerente(Funcionario):
    def __init__(self, cargo, nome,salario):
        super().__init__(cargo,nome)
        self._salario = salario
    
    
    def exibir(self):
        print(F"O seu nome e {self._nome} e seu salario e {self._salario}")