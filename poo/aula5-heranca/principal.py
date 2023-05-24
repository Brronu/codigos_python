import os
os.system("cls")
from pessoa import Pessoa, Aluno, Professor

p1 = Pessoa ("Carla", 23)
a1 = Aluno("Jose", 40)
s1 = Professor( "Gustavo", 52)

p1.relatorio()
a1.mostraAluno()
s1.mostraProfessor() 