'''
Desafio 044

Elabore um programa que calcule o valor a ser pago por um
produto, considerando o seu preço normal e condição
de pagamento:

- À vista dinheiro/ cheque: 10 de desconto
- À vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Digite o valor da venda R$ '))
print('[1] - À Vista no Dinheiro\n[2] - À Vista no Cartão\n[3] - 2x no Cartão\n[4] - 3x ou mais no Cartão')
condicao = int(input('Digite a sua opção:'))
desconto = 0

if condicao == 1:
    desconto = preco * 0.9
elif condicao == 2:
    desconto = preco * 0.95
elif condicao == 3:
    desconto = preco
elif condicao == 4:
    desconto = preco * 1.2
else:
    print('Opção inválida.')
    desconto=preco

print('Sua compra de R$ {:.2f] vai custar R$ {:.2f}'.format(preco,desconto))
