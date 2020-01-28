'''
Desafio 063

Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os n primeiros elementos de uma Sequência
de Fibonacci.

Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8
'''

print('-' * 40)
print('Sequência de Fibonacci')
print('-' * 40)
n = int(input('Quantos termos você quer mostrar? '))
print('~' * 40)

t1 = 0
t2 = 1
cont = 1

while cont <= n:
    if cont == 1:
        print(t1, end=' - ')
    elif cont == 2:
        print(t2, end=' - ')
    else:
        proximo = t1 + t2
        print(proximo, end=' - ')
        t1 = t2
        t2 = proximo
    cont += 1
print('FIM')
print('~' * 40)
