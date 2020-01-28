'''
Desafio 055

Faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o peso maior e o menor peso lidos.
'''
for c in range(1, 6):
    peso = float(input('Peso da {}a pessoa: '. format(c)))
    if c == 1:
        maior = menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso


print('O maior peso lido foi de {:.2f}Kg'.format(maior))
print('O menor peso lido foi de {:.2f}Kg'.format(menor))

