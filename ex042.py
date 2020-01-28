'''
DEsafio 042

Refaça o Desafio 035 dos triângulos acrescentando
o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais.
- Isósceles: dois lados iguais.
- Escaleno: todos os lados diferentes.
'''

print('Vamos testar se as retas foram um triângulo.')
r1 = int(input('Digite um comprimento de reta: '))
r2 = int(input('Digite um comprimento de reta: '))
r3 = int(input('Digite um comprimento de reta: '))

if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
    print('Não forma um triângulo.')
else:
    print('Você formou um trinângulo.')
    if r1 == r2 == r3:
        print('Esse triângulo é Equilátero.')
    elif r1 != r2 != r3 != r1:
        print('Esse triângulo é Escaleno.')
    else:
        print('Esse triângulo é Isósceles')