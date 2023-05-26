import os
os.system("cls")
from produto import Produto, Livro, Eletronico

l1 = Livro ("hoje e quinta", 40, "Fulano cury" )
e1 = Eletronico ("iphone", 100, "apple")

l1.descrever()
l1.calcularPreco()

e1.calcularPreco()