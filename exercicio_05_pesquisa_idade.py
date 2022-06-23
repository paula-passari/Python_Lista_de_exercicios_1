''' Em uma pesquisa para a escola, Dennis tem que entrevistar algumas pessoas e recolher alguns dados: idade média dos entrevistados, idade da pessoa mais velha, idade da pessoa mais nova e porcentagem de menores de idade. 
Crie um algoritmo para que Dennis consiga calcular e obter os dados dessa pesquisa. '''

somaIdade = 0
maisVelho = 0
maisNovo = 999
menores = 0
c = 0
totalEntrevistados = int(input('Digite o número de pessoas entrevistadas: '))
while c < totalEntrevistados:
    idade = int(input('Digite a idade da pessoa: '))
    somaIdade += idade
    if idade > maisVelho:
        maisVelho = idade
    if idade < maisNovo:
        maisNovo = idade
    if idade < 18:
        menores += 1
    c += 1

mediaIdade = somaIdade // totalEntrevistados
porcentagemMenores = (menores / totalEntrevistados) * 100

print(f'A idade média dos entrevistados é de {mediaIdade} anos')
print(f'A pessoa mais velha tem {maisVelho} anos.')
print(f'A pessoa mais nova tem {maisNovo} anos.')
print(f'{porcentagemMenores:.2f}% dos entrevistados são menores de idade.')
    