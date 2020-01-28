'''
Desafio 062

Melhore o Desafio 061, perguntando para o usuário se ele
quer mostrar mais alguns termos. O programa encerra quando
ele disser que quer mostrar 0 termos.
'''

print('Gerador de PA')
print('-=' * 20)
n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termos = int(input('Quer mostrar quantos termos: '))

cont = 1
mais = 1
while mais != 0:
    while cont <= termos:
        print(n, end=' - ')
        n = n + r
        cont += 1
    print('PAUSA')

    mais = int(input('Quantos termos você quer mostrar a mais? '))
    termos += mais
print('Progressão finalizada com {} termos mostrados'.format(termos))