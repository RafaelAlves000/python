import os
os.system('cls')

palavra= (input('insira uma paravra '))

if len(palavra) > 5:
    print("A palavra tem mais de 5 letras")
else:
    print("A palavra tem 5 letras ou menos")
