'''
Desafio 043

Desenvolva uma lógica que leia o peso e a altura
de uma pessoa, calcule seu IMC e mostre seu status,
de acorodo com a tabela abaico:

- abaixo de 18.5: Abaixo do peso
- entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: obesidade mórbida
'''
print('- ' * 15)
print('- Vamos calcular o seu IMC. -')
print('- ' * 15)

peso = float(input('Informe o seu peso Kg: '))
altura = float(input('Informe a sua altura cm: '))

altura = altura/100
imc = peso / (altura ** 2)
print('O seu IMC é de {:.2f}'.format(imc))
if imc <= 18.5:
    print('Você está abaixo peso.')
elif imc <= 25:
    print('Você está no peso Ideal. Parabéns!!')
elif imc <= 30:
    print('Cuidado você está com sobrepeso. Faça exercicios.')
elif imc <= 40:
    print('Cuidado você está obeso(a). Procure um médico!!')
else:
    print('OBESIDADE MÓRBIDA. PROCURE UM MÉDICO, URGENTE!!!!!')
