while True:
    num = int(input("Informe um valor entre 1 e 9: "))
    if num >= 1 and num <= 9:
        break

cont = 1
while cont <= 10:
    if num % 2== 0:
        print(f"{num} x {cont} = {num * cont}")
    else:
        print(f"{num} + {cont} = {num + cont}")
        
    cont +=1

    