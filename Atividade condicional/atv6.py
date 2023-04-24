percurso = float(input("Informe o percurso em km: "))
carro = int(input("Informe o tipo do carro, 1, 2 ou 3: "))

if carro == 1:
    total = percurso / 8

elif   carro == 2:
    total = percurso / 9
    
elif carro == 3:
    total = percurso / 12
   


    
    
print(f"o tipo do carro e {carro} vai precisar de {total} litros de gasolina\n")
