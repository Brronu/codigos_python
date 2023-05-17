import os
pessoa = dict()
grupo = list()


grupo.append({"nome":"João", "idade":56})
grupo.append({"nome":"Maria", "idade":27})
grupo.append({"nome":"José", "idade":32})

os.system("cls")

print(grupo,"\n")
"""
for cont in range (0,3):
    pessoa["nome"] = input("Qual seu nome: ")
    pessoa["idade"] = int(input("Qual sua idade: "))
    
    grupo.append(pessoa.copy()) #Criado copias de dicionario, sem criar vinculo ao dicionario(copianso e limpado)
print(grupo)
"""

#ACESSANDO ITENS DO DICIONARIO


for cont in range (0,3):
    print(f"{grupo[cont]['nome']}: {grupo[cont]['idade']}")

#outra forma de acessar dicionario
for linha in grupo:
    for chave, valor in linha.items():
        print(f"{chave} -- {valor}")

for linha in grupo:
    for elemento in linha.values():
        print(f"{elemento}", end="-- ")
print()

