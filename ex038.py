'''
Desafio 038
Escreva um programa que leia dois números inteiros e
compare-os, mostrando na tela uma mensagem:
o primeiro valor é maior
o segundo valor é maior
Não existe valor maior, os dois são iguais
'''

n = int(input('Digite um numero: '))
x = int(input('Digite outro numero: '))

if n > x:
    print('O Primeiro valor é maior!')
elif n == x:
    print('Não existe valor maior, os dois são iguais!')
else:
    print('O segundo valor é maior!')