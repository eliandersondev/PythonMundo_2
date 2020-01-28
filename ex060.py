'''
Desafio 060

Faça um programa que leia um número qualquer e mostre
o seu fatorial.

Ex:
5! = 5 * 4 * 3 * 2 * 1 = 120
'''

fatorial = int(input('Digite um número para calcular seu fatorial:'))
n = fatorial - 1

while n > 1:
    total = fatorial * n
    ordem = str(n) + str(n-1)
    n = n - 1
print('Calculando {}! = {} = {}'.format(fatorial, ordem, fatorial))

