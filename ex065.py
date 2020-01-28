'''
Desafio 065

Crie um programa que leia vários números inteiros pelo
teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valor lido.
O programa deve perguntar ao usuário se ele que ou não
continuar a digitar valores.
'''

continuar = 'S'
cont = soma = media = maior = menor = 0
while continuar in 'Ss':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    continuar = str(input('Quer Continuar? [S/N] '))

media = soma / cont
print('Você digitou {} números e a média foi {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))