# from calculadora import Calculadora


# exibir = Calculadora (100 , 20)

# exibir.soma()
# exibir.subtrair()
# exibir.multiplicar()
# exibir.dividir()

class Calculadora: 
    def __init__(self):
        self.__num1 = 0
        self.__num2 = 0
    
    def somar(self, valor1, valor2):
        self.__num1 = valor1
        self.__num2 = valor2

    print(f"A soma e {self.__num1 + self.__num2}")
    
           