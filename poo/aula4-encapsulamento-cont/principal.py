from funcionario import Funcionario

f1 = Funcionario ("Bruno", "Fullstack")
#f2 = Funcionario ("fumabeck", "Manutenção de ar condicionado")

print (f"Seu nome e {f1.getNome()}")
f1.setNome("Isabela")
print (f"Seu nome e {f1.getNome()}")



print(f"seu cargo e {f1.cargo}")

f1.cargo = "Gerente"

print(f"seu cargo e {f1.cargo}")

