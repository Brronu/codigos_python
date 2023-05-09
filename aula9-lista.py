notas = [9.5, 7.0, 6.5, 9]
print(notas)
print (type(notas))

for i in notas:
    print(i)

notas[2] = 8.5 #Alterando informaçao de uma lista
print("-"*30)
print(notas)

# Inserindo valores na lista
# Forma 1
notas.append(4) # vai inserir o item no final da lista
print(notas, "\n")

#Forma 2
notas.insert(3,10)# isert prescisa de 2 parametro. 1 é o indice que desejo inserir o valor. 2- é o valor propriamente dito que quero inserir
print(notas, "\n")

#Removendo valores
#forma 1
notas.pop()#excluir o ultimo elemento
print(notas, "\n")

#forma 2
notas.pop(2) # removendo pelo indice
print(notas, "\n")

#Forma 3
notas.remove(9.5)# o remove() exclui usando o condudo da lista como paramentro
print(notas, "\n")