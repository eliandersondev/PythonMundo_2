'''
Desafio 051]

Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''
print('{:=^40}'.format('Progressão Aritmética'))
n1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Qual é a razão dessa PA: '))
decimo_termo = n1 + (10 - 1) * razao
PA = []
for c in range(n1, decimo_termo + razao, razao):
    PA.append(c)

print('PA:',PA)