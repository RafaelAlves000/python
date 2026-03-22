import os 
os.system('cls')
numero = int(input("Digite um número: "))

if numero % 3 == 0:
    print(f"{numero} é múltiplo de 3.")
elif numero % 5 == 0  :
    print("multiplo de 5 ")
else:
    print('nao é multiplo de 3 e 5')


