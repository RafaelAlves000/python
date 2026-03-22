import os
os.system('cls')


print('informe 2 números')

n1 = int(input('primeiro numero '))
n2 = int(input('segundo numero '))
numeros = n1 + n2


if numeros > 100:
    print('seu valor é maior que 100')
else:
    print(f'seu valor é {numeros}')

