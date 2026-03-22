#while repeti infinito

'''
cont = 0
while True:
    cont = cont +1
    print(cont)
    if cont >= 10:
        break


sair='não'

while   sair !='sim':
  sair  = input ('deseja sair')

print('opção 0 cadastras')
print('opção 1 editar')
print('opção 2 excluir')

opcao = int(input('o que deseja realizar '))

match opcao:
    case 0:
        print('vc escolheu cadastrar')
        sair = input('deseja sair')
    case 1:
        print('editar')
        sair = input('deseja sair')
    case 2:
        print('excluir')
        sair = input('deseja sair')
    case _:
        print('opção invalida')
        sair = input('deseja sair')
'''

#for para repetições pre definidas de vezes.

for numero in range(10):
    print(numero)

percorrer lista
frutas= ['uva', 'maça', 'melao', 'pera']

for fruta in frutas:
    print(fruta)
.
if else
#solicitando dados do usuario
  # nome = input('digite seu nome:')
   #idade = int(input('digite sua idade:'))
   #altura = float (input('digite sua altura:'))

idade= float(alutra)
   #print(f'seu nome é {nome}, sua idade é {idade}, e vc tem {altura} de altura')

  # print(type(idade)) 
   #print(type(altura))

  #condicional if else

   #acompanhada = 'nao'

#if idade <= 0:
 #   print("invalida")
if  idade >=18:
print("vc é pode assistir o filme")
elif idade <15:
print("vc nao pode assistir o filme")
elif idade <=17:
if acompanhada == 'sim':
print('vc pode assistir')
else:
print('vc nao pode assistir o filme')
else :
print("dados invalido")
if idade >=18:
print('pode')
elif (idade >=15 and idade <=17) and acompanhada == 'sim':
print('vc pode assistir')
   #else: print('vc n pode assistir')


print('opção 0 cadastras')
print('opção 1 editar')
print('opção 2 excluir')

opcao = int(input('o que deseja realizar '))

match opcao:
    case 0:
        print('vc escolheu cadastrar')
    case 1:
        print('editar')
    case 2:
        print('excluir')
    case _:
        print('opção invalida')
.
.
.
.
.
.
..
criar função
def soma (numero1, numero2):
    """
    essa função recebe 2 numeros e realiza a soma.

    """

    soma = numero1 + numero2
    print(f'o resumato da soma é {soma} ')

soma(4, 7)

def sub (numero1, numero2):
    """
    essa função recebe 2 numeros e realiza a subtração.

    """

    sub = numero1 - numero2
    print(f'o resumato da soma é {sub} ')

sub(4, 7)

def menu():
    print('1 - somar ')
    print('2 - sub ')
    opcao = input('o que deseja realizar? ')
    return opcao
.
.
.
.
.
.
importa função
import os  #serve para limpar o terminal

from funcao import soma, sub, menu  #importar função de outras arquivos

continuar = 's'
while continuar != 'n':

    os.system('cls')
    opcao = menu()



    numero1 = int(input("informe o primeiro numero  "))

    numero2 = int(input("informe o segundo numero  "))

    if opcao == '1':
        soma(numero1, numero2)

    elif opcao == '2':
        sub(numero1, numero2)
    else:
        print('opção invalida')



    continuar = input( 'deseja realizar mais somas s ou n ')
.
.
.
.
.
.
lista
#nomes = ['rafel', 'lucas',]

#print(nomes[1])

apostolos = ['math','judas','tiago', 'lucas', 'judas', 'pedro']

#percorrendo lista

for apostolo in apostolos:
    print(apostolo)

#adicionar intens na lista/em uma posição
apostolos.append('joao')
print(apostolos)

apostolos.insert(2,'rafael')
print(apostolos)



cavaleiros = ['seya', 'shiryu']
print(cavaleiros)

cavaleiros.extend(['ikki','yoga','shun'])
print(cavaleiros)

#excluir itens da lista

cavaleiros.pop(2)
print(cavaleiros)

#excluindo o valor

#apostolos.remove("judas")
print(apostolos)

for indice,apostolo in enumerate(apostolos):
    if apostolo == 'judas':
        apostolos.pop(indice)

print(apostolos)

pares = []
numeros = [1,2,3,4,5,6,7,8,9,10]
impares = []
for numero in numeros:
    if numero % 2 != 0:
        impares.append(numero)
    elif numero % 2 == 0:
        pares.append(numero)

print(pares)
print(impares)

apostolos.sort()
print(apostolos)

cavaleiros.clear()
print(cavaleiros)

del pares
VelhoSolitárioS2 — 19/03/2026 21:17
.
.
.
..
.
..
..
.
.
logica
#criando variaveis

nome = 'aluno'

idade = 100
altura = 1.40
adulto = True
digitar no console
print(nome)
print(idade)

concatenado
print ('oi ' + nome)

print( 'meu nome é ', nome,'e tenho ', idade, 'anos')

print(f'meu nome é {nome} e tenho {idade} anos')

#verificando o tipo da variavel
#print(type(nome))
#print(type(idade))
#print(type(altura))

#Expressoes logicas

numero1 = 10
numero2 = 2

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2 

print(f' a soma é {soma}')
print(f' a subtração é {subtracao}')
print(f' a multiplicação é {multiplicacao}')
print(f' a divisão é {divisao}')

exp = numero1 + (numero2 * numero2) - numero1

print(exp)

#outras expressoes logicas

potencia = numero1 ** numero2
resto = numero1 % numero2
div_exata = numero1 // numero2

print(potencia)
print(resto)