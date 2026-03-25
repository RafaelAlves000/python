import os
os.system('cls')

numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

soma = sum(numeros)

print("Soma dos números:", soma)