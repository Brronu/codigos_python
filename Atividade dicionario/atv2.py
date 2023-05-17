lista = list ()
telefone = dict ()

for cont in range (0,7):
    nome = input("Informe seu nome: ")
    telefone[nome] = int(input(f"Informe o numero de telefone {nome}: "))

    lista.append(telefone.copy)
    telefone.clear()
print()