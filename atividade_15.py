import os 

nota = int(input('me informe sua idade: '))

os.system('cls')


if  nota <13:
    print('criança')
elif 13 <= nota <= 17:
    print('adolecente')
else:
    print('adulto')