'''
Desafio 070

Crie um programa que leia o nome e o preço de
vários produtos. O programa deverá perguntar se o
usuário vai continuar.
No final, mostre:

A - Qual é o total gasto na compra.
B - Quantos produtos custam mais de R$ 1000,00
C - Qual é o nome do produto mais barato.
'''

print('-' * 50)
print('{:^50}'.format('LOJA SUPER BARATÃO'))
print('-' * 50)

menor_produto = ''
cont = menor_preco = total = quant_mais_mil = 0

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco

    if preco > 1000:
        quant_mais_mil += 1
    if cont == 1 or preco < menor_preco:
        menor_preco = preco
        menor_produto = produto

    continuar = 'x'
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print('{:-^50}'.format(' FIM DO PROGRAMA '))
print('O total da compra foi R$ {:.2f}'.format(total))
print('Temos {} produtos custando mais de R$ 1000.00'.format(quant_mais_mil))
print('O produto mais barato foi {} que custa R$ {:.2f}'.format(menor_produto, menor_preco))