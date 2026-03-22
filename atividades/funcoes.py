def soma (n1, n2):

    soma = n1 + n2
    print(f'o resultado da soma é {soma} ')
def sub (n1, n2):

    sub = n1 - n2
    print(f'o resultado da sub é {sub} ')
def vezes (n1, n2):

    vezes = n1 * n2
    print(f'o resultado da multiplicação é {vezes} ')
def div (n1, n2):

    div = n1 / n2
    print(f'o resultado da div é {div} ')

def menu():
    print('1 - somar ')
    print('2 - sub ')
    print('3 - vezes ')
    print('4 - divisao ')
    opcao = input('o que deseja realizar? ')
    return opcao

def locomocao():
    print('1 - carro')
    print('2 - bicicleta')
    print('3 - pé')
    meios = int(input('qual meio de transporte? '))
    return meios


def valores (valor):
    match valor:
        case int(x) if x > 0:
            return f"{x} é um inteiro positivo"
        case int(x) if x < 0:
            return f"{x} é um inteiro negativo"
        case 0:
            return "É zero"
        case _:
            return "Não é um inteiro válido"