import os 

nota = int(input('me de uma nota de 0 a 10: '))

os.system('cls')


if 0<= nota <= 4:
    print('baixo')
elif nota == 5:
    print('media')
elif 6 <= nota <= 10:
    print('alta')
else:
    print('erro')