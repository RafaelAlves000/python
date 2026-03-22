import os
os.system('cls')

numero = int(input('informe um valor '))


match numero:
        case x if x> 10:
            print(f"{numero} o valor é maior que 10 ")
        case x if x< 10:
            print(f"{numero} o valor é menor que 10 ")
        case x if x ==10:
            print(f"{numero} o valor é igual que 10 ")
        case _:
            print ('erro') 