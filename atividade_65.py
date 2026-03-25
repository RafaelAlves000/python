import os
os.system('cls')

numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

print("Maior número:", maior)
print("Menor número:", menor)