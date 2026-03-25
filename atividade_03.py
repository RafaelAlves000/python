import os 

semanas = int(input('Que dia é hoje onde 1 correposnde a segunda até o 7 que corresponde domingo'))

os.system('cls')
match semanas:
        case 1:
            print('Segunda')
        case 2:
            print('Terça')
        case 3:
            print('Quarta')  
        case 4:
            print('Quinta')
        case 5:
            print('Sexta')
        case 6:
            print('Sabado')
        case 7:
            print('Domingo')