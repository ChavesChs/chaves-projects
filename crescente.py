print("Digite dois numeros:")
valor1 = int(input())
valor2 = int(input())

while valor1 != valor2:
    
    if valor1 > valor2:
        print("Descrescente")
    else:
        print("Crescente")

    print("Digite novos dois numeros:")

    valor1 = int(input())
    valor2 = int(input())
