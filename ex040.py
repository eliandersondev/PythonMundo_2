'''
Desafio 040

Crie um programa que leia duas notas de um aluno e calcule
sua média, mostrando uma mensagem no final, de acordo
com a média atingida:

- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Você está reprovado! A sua média foi de {:.2f}.'.format(media))
elif media < 7:
    print('Você está em Recuperação! A sua média foi de {:.2f}.'.format(media))
else:
    print('Meus Parabéns, você está Aprovado!!! A sua média foi de {:.2f}.'.format(media))