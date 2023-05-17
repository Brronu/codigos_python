import os
estado = {"uf": "Maranhão", "Sigla": "MA"}

os.system("cls")
print (estado)

# FORMA 1: ISERINDO DADOS EM UM DICIONARIO
estado["populacao"] = "20.000.000"
print(estado)

#FORMA 2: 
estado.update({"capital":"São Luis"})
print (estado)

#REMOVEMDO ITENS DO DICIONARIO
#FORMA 1
estado.pop("uf")
print(estado)

#FORMA 2
del(estado["populacao"])
print (estado)

#FORMA 3 - APAGAR TODO CONTEUDO
"""estado.clear()
print(estado)"""
          