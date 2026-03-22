import os
os.system('cls')

numero1 = int(input('insira o primeiro valor '))

numero2 = int(input('insira o segundo valor '))

numero3 = int(input('insira o terceiro valor '))



maior = numero1

if numero2 > maior:
    maior = numero2

if numero3 > maior:
    maior = numero3

print("O maior número é:", maior)