playlist = list ()
musica = dict ()

for cont in range(2):
    nome = input("Qual o nome da musica: ")
    artista = input("Qual o nome do artista: ")
    tempo = float(input("Qual a duração da musica? "))

    musica[nome] = {"Artista": artista, "Duracao": tempo}

    playlist.append(musica.copy())
    musica.clear()
print(playlist)
for linha in playlist:
    for chave, valor in linha.items():
        print(f"{chave}: {valor['Artista']} Duração:{valor['Duracao']}")
        
