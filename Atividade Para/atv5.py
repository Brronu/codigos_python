valor = int(input("informe um valor qualquer: "))

maior = 0
posicao = 0

for cont in range(1, valor + 1):
    item = int(input("informe um valor: "))
    if item >= maior:
        maior = item
        posicao = contador 

print(f"O maior valor é {maior} e esta na posição{posicao}\n") 

