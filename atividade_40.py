import os
os.system('cls')

numero1 = int(input('insira o primeiro valor: '))

numero2 = int(input('insira o segundo valor: '))

numero3 = int(input('insira o terceiro valor: '))



if numero1 == numero2 and numero2 == numero3 :
    print("todos numeros são iguais")
else:
    print('algum numero é diferente')