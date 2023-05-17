lista = list()
preco = dict()
for cont in range (0,8):
    pratos = input("Informe o nome dos prato: ")
    preco [pratos] = int(input(f"informe o valor do prato {pratos}: "))

    lista.append(preco.copy())

    preco.clear()


