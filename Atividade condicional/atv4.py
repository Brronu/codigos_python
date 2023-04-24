salario = float(input("Informe seu salário: "))
F = float(input("Qual o valor do financiamento: "))

Valor5x = F * 5

if Valor5x <= salario: 
    print("Finamciamento concedido\n")
else:
    print("Financiamento não concedido\n")

print("obrigado por nos consultar\n")