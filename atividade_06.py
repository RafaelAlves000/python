
from funcoes import soma, sub, menu, vezes, div

opcao = menu()



n1 = int(input("informe o primeiro numero  "))

n2 = int(input("informe o segundo numero  "))

if opcao == '1':
        soma(n1, n2)

elif opcao == '2':
        sub(n1,n2)

elif opcao =='3':
        vezes(n1, n2)

elif opcao == '4':
    div(n1,n2)
else:
        print('opção invalida')