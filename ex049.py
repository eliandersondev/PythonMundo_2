'''
Desafio 050

Refaça o Desafio 009, mostrandi a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for.
'''

tabuada = int(input('Digite um número inteiro para mostrar a tabuada: '))
print('-' * 15)
for c in range(1,11):
    print('{} x {:2} = {:3}'.format(tabuada,c,tabuada*c))
print('-' * 15)
