mediaTurma = 0
mediaMulheres = 0
somaTurma = 0
somaMulheres = 0
contMulheres = 0

for cont in range(1,7):
    altura = float(input("Informe sua altura: "))
    sexo = int(input("Informe o codigo do sexo: 1-masc ou 2-fem: "))

    if cont == 1: 
        menor = altura
        maior = altura
    else: 
        if altura >= maior:
                maior = altura

        if altura <= menor:
                menor = altura

    if sexo == 2:
        somaMulheres += altura
        contMulheres += 1

    somaTurma += altura 

print (f"A maior altura e {maior} e a menor altura é {menor}")
print (f"A media de altura das mulheres e {somaMulheres / contMulheres}")
print (f" A media de altura da turma e {somaTurma / 6}\n")
