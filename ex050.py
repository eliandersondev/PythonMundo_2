'''
Desafio 050

Desenvolva um programa que leia seis números e mostre
a soma apenas daqueles que forem pares. Se o valor digitado foi
ímpar, desconsidere-o.
'''

soma = 0
for c in range(6):
    valor = int(input('Digite um número inteiro: '))
    if valor % 2 == 0:
        soma += valor

print('A soma é : ', soma)
