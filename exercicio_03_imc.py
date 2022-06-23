''' IMC é a sigla para Índice de Massa Corpórea, parâmetro adotado pela Organização Mundial de Saúde para calcular o peso ideal de cada pessoa. O índice é calculado dividindo o peso de uma pessoa pela sua altura elevada ao quadrado. Faça um programa que calcule o IMC de uma pessoa. 
Considere: 
Abaixo de 17 = Muito abaixo do peso
Entre 17 e 18.49 = Abaixo do peso
Entre 18.5 e 24.99 = Normal
Entre 25 e 29.99 = Sobrepeso
Entre 30 e 34.99 = Obesidade I
Entre 35 e 39.99 = Obesidade II (severa)
Acima de 40 = Obesidade III (mórbida) '''

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)

if imc < 17:
    print(f'Seu IMC é {imc:.2f}. Você está muito abaixo do peso ideal.')
elif imc < 18.5:
    print(f'Seu IMC é {imc:.2f}. Você está abaixo do peso ideal.')
elif imc < 25:
    print(f'Seu IMC é {imc:.2f}. Você está no peso ideal.')
elif imc < 30:
    print(f'Seu IMC é {imc:.2f}. Você está acima do peso ideal')
elif imc < 35:
    print(f'Seu IMC é {imc:.2f}. Você está com Obesidade grau I')
elif imc < 40:
    print(f'Seu IMC é {imc:.2f}. Você está com Obesidade grau II (severa)')
else:
    print(f'Seu IMC é {imc:.2f}. Você está com Obesidade grau III (mórbida)')