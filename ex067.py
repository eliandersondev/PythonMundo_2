'''
Desafio 067

Faça um programa que mostre a tabuada de vários números, um
de cada fez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado
for negativo.
'''
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break

    print('-' * 40)
    for c in range(1, 11):
        print('{:3} x {:3} = {:3}'.format(n, c, n * c))

    print('-' * 40)



print('Programa TABUADA ENCERRADO. Volte Sempre!')
