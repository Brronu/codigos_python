a = float(input("Informe o lado A: "))
b = float(input("Informe o lado B: "))
c = float(input("Informe o lado C: "))

if a < b+c and b < a+c and c < a+b:
    print("temos um triângulo\n")
else:
    print("Você  não encotrou um triagulo\n")
