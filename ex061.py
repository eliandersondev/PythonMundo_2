'''
Desafio 061

Refaça o Desafio 051, lendo o primeiro termo e a razão
de uma PA, mostrando os 10 primeiros termos da
progressão usando a estrutura while.
'''
print('Gerador de PA')
print('-=' * 10)
n = int(input('Primeiro termo:'))
razao = int(input('Razão da PA: '))

cont = 1
termo = n

while cont <= 10:
    print('{}'.format(termo), end=' - ')
    cont += 1
    termo = termo + razao

print('FIM')

decimo = n + (10 - 1) * razao

for c in range(n, decimo +1, razao):
    print('{}'.format(c), end='')
    print(' - ' if c < decimo else '', end='')

print('\nUSANDO WHILE')
cont = n
while cont <= decimo:
    print('{}'.format(cont), end='')
    print(' - ' if cont < decimo else '', end='')
    cont += razao

