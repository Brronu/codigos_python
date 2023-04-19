texto = "Técnico em Desenvolvimento de sistema"
print("*****Titulo*****")
print("*"*10)
print(texto)

'''idade = int(input(f"Qual sua idade: "))
print(idade)
print("# "*idade)
'''

#manipulando texto(string)
print(f"o total de letras é: {len(texto)}")#len() vem de length, que significa total

print(texto.lower()) # lower() coloca tudo texto em minusculo
print(texto.upper()) # upper() coloca tudo texto em maiusculo
print(texto.capitalize()) # capitalize() coloca a 1ª letra em maiusculo

print(texto.replace("sistema", "web"))# replace troca um txto por outro

#TRABALHADO COM FATIAMENTO 

print("Fatiando a variavel texto")
print(texto[:4])#Vai exibir todo o texto ate a posição 2, no caso a posição 3 n conta.
print(texto[4:])#Vai exibir todo o texto a partir da posição 3
print(texto[4:10])#vai exibir todo o texto esta na posição 3 ate 10