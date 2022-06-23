''' Crie um algoritmo que preencha uma lista com números aleatórios e que crie uma segunda lista e preencha com os valores da primeira lista mas em ordem reversa. 
ATENÇÃO: não pode usar a função reverse() '''

import random

# preencher lista 1 com números aleatórios
numeros = int(input('Quantos números deseja colocar na lista? '))
lista1 = []
number = 0

for i in range(numeros):
    number = random.randint(1,99)
    if number not in lista1:
        lista1.append(number)

# preencher lista 2 com números da lista 1 de forma inversa
lista2 = []
for x in lista1[::-1]:
    lista2.append(x)
    

print(lista1)
print(lista2)