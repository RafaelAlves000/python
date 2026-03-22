import os 
os.system('cls')


idade = int(input('informe sua idade para acessar o site '))

if idade >=18:
    print('maior de 18 pode acessar seu site duvidoso')
elif idade <18:
    print(' menor de idade Banido')
else:
    print('erro')