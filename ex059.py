'''
Desafio 059

Crie um programa que leia dois valores e mostre um menu
na tela:

[1] somar
[2] multiplicar
[3] maior
[4] Digitar novos números
[5] sair do programa

Seu programa deverá realizar a operação
solicitada em cada caso.
'''
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 1
while opcao != 5:
    print('\n{:=>40}'.format('Calculadora Prática\n'))
    print('[1] somar\n[2] multiplicar\n[3] maior\n[4] Digitar novos números\n[5] sair do programa')
    opcao = int(input('\nQual é a sua opção? '))
    if opcao == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('O maior número é {}.'.format(n1))
        elif n1 < n2:
            print('O maior número é {}.'.format(n2))
        else:
            print('Os números são iguais.')
    elif opcao == 4:
        print('Informe outros números')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Até a próxima!')
    else:
        print('Opção Inválida! Tente novamente.')