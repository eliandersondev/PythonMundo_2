'''
Desafio 053

Crue um programa que leia juma frase qualquer e diga
se ela é um palíndromo, desconsiderando os espaços.
'''

frase = str(input('Digite uma frase: ')).upper().replace(' ', '')
tamanho = len(frase)
cont = 0
palindromo = False

#Esse foi o meu jeito de resolver
for c in frase:
    cont += 1
    for x in range(tamanho-cont, -1, -1):
        if c == frase[x]:
            palindromo = True
            break
        else:
            palindromo = False
            break
print('A frase é {} Palindromo.'.format(palindromo))

#outra forma
inverso = frase[::-1]

# Esse é outro
inverso=''
for c in range(tamanho-1, -1, -1):
    inverso += frase[c]
if frase == inverso:
    print('Temos um palindromo!')
else:
    print('Não temos um palindlromo!')



