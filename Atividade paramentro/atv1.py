b = int(input("Informe sua idade: "))

def idade (a):
    if a >= 5 and a <= 7:
        return("INFANTIL A")
    
    elif a >= 8 and a <= 10:
        return("INFANTIL B")
    
    elif a >= 11 and a <= 13:
        return("JUVENIL A")
    
    elif a >= 14 and a <= 17:
        return("JUVENIL B")
    
    elif a >= 18:
        return("ADULTO")
        
print(idade(b))

