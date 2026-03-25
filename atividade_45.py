import os
os.system('cls')



maior = None

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    
    if maior is None or numero > maior:
        maior = numero

print(maior)
        
