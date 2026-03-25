import os
os.system('cls')

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

while num1 <= num2:
    print("O primeiro número NÃO é maior que o segundo. Tente novamente.\n")
    
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

print("Agora sim! O primeiro número é maior que o segundo.")