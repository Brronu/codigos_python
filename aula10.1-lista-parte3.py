#import random
from random import randint 
import os

os.system("cls")
sorteio = []

for cont in range (1,11):
    sorteio.append(randint(1,100))# gerando valores aleatorios e salvado na lista

#valor = randint(1,100)# essa função ira gerar um número aleatorio entre 1 e 100
print (sorteio)
print (sorteio.sort(reverse=True)) # a função sort() ordena de forma crescente. O paramentro reverse=True, faz o contrario, ordena de forma decrescente
print (sorteio)
os.system("pause")# ira pausar o sistema ate uma tecla ser pressionada