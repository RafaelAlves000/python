import os
os.system('cls')

contador = 0

for i in range(7):
    numero = int(input(f"Digite o {i+1}º número: "))
    
    if numero > 10:
        contador += 1

print(f"Quantidade de números maiores que 10: {contador}")