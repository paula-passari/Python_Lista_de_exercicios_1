''' Faça um programa que receba a velocidade que um veículo passou no radar e mostre quantos pontos na carteira o condutor vai levar. Considere:
Infração Leve: 50km/h - 3 pontos
Infração Média: 65km/h - 4 pontos
Infração Grave: 80km/h - 5 pontos
Infração Gravíssima: 100km/h - 7 pontos
Considere também que o radar tem tolerância de 10% sobre a velocidade na Infração Leve. '''

inf_leve = 50 * 1.1     # 1.1 representa o acréscimo, a tolerância de 10% da velocidade
inf_media = 65
inf_grave = 80
inf_gravissima = 100

velocidade = float(input('Informe a velocidade que o veículo passou no radar: '))

if velocidade <= inf_leve:
    print(f'O veículo passou no radar a {velocidade} km/h. Isento de multa.')
elif velocidade < inf_media:
    print(f'O veículo passou no radar a {velocidade} km/h. Infração Leve: 3 pontos.')
elif velocidade < inf_grave:
    print(f'O veículo passou no radar a {velocidade} km/h. Infração Média: 4 pontos.')
elif velocidade < inf_gravissima:
    print(f'O veículo passou no radar a {velocidade} km/h. Infração Grave: 5 pontos.')
else:
    print(f'O veículo passou no radar a {velocidade} km/h. Infração Gravíssima: 7 pontos.')