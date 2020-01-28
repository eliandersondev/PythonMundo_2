'''
Desafio 037
Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:

1 para binário
2 para octal
3 para hexadecimal
'''
n = int(input('Digite um número Decimal: '))
print('Esse número em binário é {}'.format(bin(n)))
print('Esse número em octal é {}'.format(oct(n)))
print('Esse número em hexadecimal é {}'.format(hex(n)))