import os 
os.system('cls')

soma = 0

for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero

media = soma / 10

print(f"Média dos números: {media}")