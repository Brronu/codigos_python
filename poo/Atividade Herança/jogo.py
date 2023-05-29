class Personagem: 
    def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = 5

    def atacar(self):
        print(f"O {self.__nome} esta atacando")

   
   
class Jogador(Personagem):
    pass


        