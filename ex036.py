'''
Desafio 036
Escreva um programa para aprovar o empréstimo bancário para
compra de uma casa. O programa vai perguntar o
valor da casa, o salário do comprador e em quantos anos
ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não
pode exceder 30% do salário ou então o empréstimo será
negado.
'''

casa = float(input('Qual é o valor da casa desejada? R$ '))
salario = float(input('Qual é o seu salário? R$ '))
anos = int(input('Em quantos anos será o financiamento? '))

margem = salario * 0.3
mensalidade = casa / (anos * 12)

if mensalidade <= margem:
    print('Meus Parabéns, o empréstimo foi concedido!'
    '\nA parcela do empréstimo ficou em R$ {:.2f}.'.format(mensalidade))
else:
    print('Infelizmente o empréstimo não foi liberado '
    '\na sua margem é de R$ {:.2f} \ne a parcela é de '
    '{:.2f}. \nNão sendo compatível com a sua renda.'.format(margem,mensalidade))