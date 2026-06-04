nome: str
genero: str
idade: int
salario: float
altura: float
vivo: bool

nome = str(input('Digite seu nome: '))
genero = str(input('Digite seu genero: '))
idade = int(input('Digite sua idade: '))
salario = float(input('Digite seu salario: '))
altura = float(input('Digite sua altura: '))
vivo = True


print(f"Nome: {nome}")
print(f"Genero: {genero}")
print(f"idade: {idade}")
print(f"Salario: {salario:.2f}")
print(f"Altura: {altura:.2f}")
print(f"Prova de vida: {vivo}")

print("O funcionario(a) {:s}, genero {:s}, idade {:d}, ganha o salario de {:.2f}, tem {:.2f} de altura".format(nome, genero, idade, salario, altura))