class Funcionario:
    def __init__(self, nome,cargo):
        self.__nome = nome
        self.__cargo = cargo

    def exibir(self):
        print (f"Ola {self.__nome} o seu cargo e {self.__cargo}")


    def getNome(self):
        return self.__nome
    
    def setNome(self, valor):
        self.__nome = valor

    # Criando o get do cargo
    @property # esse elemento ira criar um get mais amigavel
    def cargo(self):
        return self.__cargo 

    @cargo.setter # dessa forma ira cria um set para cargo mais amigavel
    def cargo(self, info):
        self.__cargo = info 
