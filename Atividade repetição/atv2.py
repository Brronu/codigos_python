cont = 1
totalHotel = 0
somaHotel = 0
while cont <= 8:
    nome = input("Informe seu nome: ")
    dias = int(input("Quantas dias você ficou no hotel? "))

    totalDiarias = dias * 50
    if dias < 15:
        taxa = dias * 4

    elif dias == 15:
        taxa = dias * 3.60

    elif dias > 15:
        taxa = dias * 3
            
            
    totalHotel = totalDiarias + taxa # o valor hotel vai receber
    print (f"Ola {nome} você ficou {dias} dias e vai pagar R$ {totalDiarias + taxa}")
    somaHotel += somaHotel

print(f"O hotel ira receber um total de R${totalHotel}")








    