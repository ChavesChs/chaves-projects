print("Dados da primeira pessoa")
nome = str(input("Nome: "))
idade1 = int(input("Idade: "))

print("Dados da segunda pessoa")
nome2 = str(input("Nome: "))
idade2 = int(input("Idade: "))

media = (idade1 + idade2) / 2

print(f"A idade media de {nome} e {nome2} e de {media:.1f} anos")