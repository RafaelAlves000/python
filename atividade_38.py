import os
os.system('cls')

altura = float(input('informe sua altura '))


match altura:
        case x if x> 1.75:
            print(f"vc tem mais de 1.75  ")
        case _:
            print (f'vc tem {altura} de altura') 