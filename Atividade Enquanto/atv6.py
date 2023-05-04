import os # importando bilioteca  para trabalhar com sistema operacional
dentroIntervalo = 0
foraIntervalo = 0
cont = 1

os.system("cls") # irá limpa a tela
while cont <= 5:
    valor = int(input(f"informe o valor {cont}: "))
    if valor >=10 and valor <=20: 
         dentroIntervalo += 1
    else:
        foraIntervalo += 1
    cont += 1

print(f"Valores dentro do intervalo: {dentroIntervalo}")
print(f"Valores fora do intervalo: {foraIntervalo}")


