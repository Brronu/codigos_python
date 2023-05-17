import os
lista = list()
produtos = dict()
os.system("cls")
for cont in range(0,5):
    nome = input("Informe o nome do produto: ")
    produtos[nome] = int(input(f"Informe a quantidade de {nome}: "))

    lista.append(produtos.copy())# copiar o conteudo do dicionario para a lista 
    produtos.clear() #limpar o conteudo do dicionario
print(lista)
