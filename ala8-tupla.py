lanche = ("pizza","hot dog", "refri", "batata", )
print(lanche)
print(type(lanche)) # Estou mostrando o tipo da variável

print(lanche[3])
print(f"o total de laches é {len(lanche)} \n")

#lanche[2] = "Suco"

for cont in range(0, 4):
    print (lanche[cont])

print("-"*30)
for i in lanche:
    print(i)

print("-"*30)
# enumerate serve para permitir acessar os indices da tupla. ja a variavel
# indice, ira armazenar os valores do indice    
for indice,e in enumerate(lanche):
    print (f"{indice} = {e}")












l.kklllklil