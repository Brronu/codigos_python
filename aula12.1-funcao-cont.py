# FUNÇÃO COM RETORNO
import os

os.system("cls")
nome = input("Informe seu nome: ")

def contarLetras(texto):
    #print(f"o nome possui o total de letras de {len(texto)} letras")
    return len(texto)

print(contarLetras(nome))