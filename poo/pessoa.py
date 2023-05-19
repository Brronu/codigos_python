import os
os.system("cls")
class Pessoa:
    # atributos
    nome = "Bruno"
    idade = 23
    altura = 1.78

    #métodos
    def falar(self, texto): # self e um paramentro pbrigatorio do python que informa que o metodo pertence a propria classe que foi criada
        print (texto)

pessoa1 = Pessoa()
pessoa1.nome = "João"

print (f"o seu nome e {pessoa1.nome}, a sua altura e {pessoa1.altura}")

pessoa1.falar("Ola mundo")
