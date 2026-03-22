import os
os.system('cls')



tipo = input("Escolha (gasolina, diesel,etanol): ")

match tipo:
    case "gasolina":
        print("7,22 por litro")
    case "diesel":
        print("R$ 6,46 por litro")
    case "etanol":
        print("R$ 5,19 por litro")
    case _:
        print("Opção inválida!")