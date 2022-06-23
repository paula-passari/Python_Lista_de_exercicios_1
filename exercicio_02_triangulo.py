''' Faça um algoritmo que receba 3 lados de uma figura e verifique se a figura é um triângulo e, se for, verifique se é um triângulo equilátero, um triângulo isósceles ou um triângulo escaleno. Para ser um triângulo, um lado da figura não pode ser maior que a soma dos outros dois lados.
O triângulo equilátero possui os três lados iguais, o triângulo isósceles possui 2 lados iguais e o triângulo escaleno possui todos os lados diferentes. '''

lado1 = float (input('Digite o 1º lado da figura: '))
lado2 = float (input('Digite o 2º lado da figura: '))
lado3 = float (input('Digite o 3º lado da figura: '))

if lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado1 + lado2:
    print('A figura não é um triângulo.')
elif lado1 == lado2 and lado2 == lado3:
    print('A figura é um triângulo equilátero.')
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print('A figura é um triângulo isósceles.')
else:
    print('A figura é um triângulo escaleno.')