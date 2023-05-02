inicial = int(input("imforme um valor inicial: "))
final = int(input("imforme um valor inicial: "))
soma = 0

for cont in range (inicial, final + 1):
    soma = soma + cont

print (f"A soma de {inicial} + {final} é {soma}\n")
