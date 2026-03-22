import os  
os.system('cls')

from funcoes import locomocao


meios = locomocao()

match  meios:
    case 1:
        print("velocidade de 20 a 40 km/h ")
    case 2:
        print('velocidade de  15 a 25 km/h.')
    case 3:
        print('velocidade de 4 a 6 km/h.')
