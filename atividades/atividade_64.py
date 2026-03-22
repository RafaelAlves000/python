
import os
os.system('cls')


import random

numeros = []

# Gerando 10 números aleatórios (de 1 a 100)
for i in range(10):
    numero = random.randint(1, 100)
    numeros.append(numero)

print("Lista:", numeros)

print("Múltiplos de 3:")

for n in numeros:
    if n % 3 == 0:
        print(n)