#while funcionando como loop contado
cont = 1

while cont <=5:
    print(cont)
    cont =cont + 1

#while funcionado como loop condicional
'''
senha = ""
while senha != "1234":
    senha = input("Informe sua senha:")

print("Obrigado por usar o sistema\n")
'''

#while como se fosse o faça - enquanto

while True:
    senha = input("informe sua senha: ")
    if senha =="1234":
        break