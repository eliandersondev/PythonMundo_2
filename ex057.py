'''
Desafio 057

Faça um programa que leia o sexo de uma pessoa, mas só
aceite os valor 'M' ou 'F'. Caso esteja errado peça
a digitação novamente até ter um valor correto.
'''

print('{:=^40}'.format(' Cadastro de Pessoas '))

sexo = str(input('Informe o seu sexo: [M/F]')).strip().upper()

while sexo not in 'MmFf':
    sexo = str(input('Dados Inválidos. Informe o seu sexo: [M/F]')).strip().upper()
print('Sexo {} registrado com sucesso.'.format(sexo))
