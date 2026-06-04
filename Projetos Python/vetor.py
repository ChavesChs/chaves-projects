N = int(input("Quantos numeros deseja digitar?"))

vet: list[float] = [0 for x in range(N)]

for i in range(0, N):
    vet[i] = float(input(f"Digite o numero {i}: "))

print()
print("NUMEROS DIGITADOS")
for i in range(0, N):
    print(f"{vet[i]:.1f}")