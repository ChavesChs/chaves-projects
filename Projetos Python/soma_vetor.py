N = int(input("Quantos numeros voce vai digitar? "))

vetor = [0 for x in range(N)]

for i in range(0, N):
    vetor[i] = float(input("Digite um numero: "))

print()
print(f"Valores =", end="")

for i in range(0, N):
    print(f"{vetor[i]:.1f} ", end="")

print()

soma = 0
for i in range(0, N):
    soma = soma + vetor[i]

print(f"SOMA = {soma:.2f}")

media = soma / N
print(f"MEDIA = {media:.2f}")
