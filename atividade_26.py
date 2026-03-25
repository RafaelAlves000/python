import os
os.system('cls')

numero1 = int(input('informe 1 valro '))

numero2 = int(input('informe outro valro '))

if numero1 % 10 in (0, 5) and numero2 % 10 in (0, 5) :
    print("multiplo de 5 ")
else:
    if numero1 % 5 != 0:
        print("O primeiro número não é múltiplo de 5")
    if numero2 % 5 != 0:
        print("O segundo número não é múltiplo de 5")