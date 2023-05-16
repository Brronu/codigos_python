lista = ["João", 30, "Cohab"]
pessoa = {
    "nome":"Bruno",
    "idade": 25,
    "bairro":"Renascença"
}

print(lista[0])
print(pessoa,"\n")

#EXIBINDO AS CHAVES UTILIZANDO O COMANDO KEYS()
print(pessoa.keys())

#EXIBINDO OS VALORES UTILIZANDO O COMANDO VALUES()
print(pessoa.values())

#EXIBINDO OS TANTO A CHAVE COMO VALOR UTILIZANDO O COMANDO ITEMS()
print(pessoa.items())

# EXIBINDO o dicionario mais detalhado
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")