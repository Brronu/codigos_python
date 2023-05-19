class Aluno:
    def __init__(self, nome, matricula, telefone):
        self.nome = nome
        self.matricula = matricula
        self.telefone = telefone

    def exibirDados(self):
        print(f"Ola {self.nome} a sua mtricula e {self.matricula} seu telefone {self.telefone}")

