class Pessoa:# superclasse ou classe mãe 
    def __init__(self,nome, idade):
        self._nome = nome # Ao utilizar 1 underline, dizemos que o atributo esta com            modificador protegido, ou seja, as classe filhas tem acesso filhas tem acesso aos atributos da classe mãe.
        self._idade = idade

    def relatorio (self):
        print("sou uma pessoa")
        print(f"Ola {self._nome}, sua idade e {self._idade}\n") 

class Aluno (Pessoa):
    def mostraAluno(self):
        print(f"Sou aluno e meu nome e {self._nome}")


class Professor (Pessoa):
    def mostraProfessor(self):
        print (f"Sou professor meu nome e {self._idade}")