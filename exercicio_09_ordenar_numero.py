''' Crie um algoritmo com uma lista que deve ser preenchida com números aleatórios. Reordene a lista de forma crescente.
ATENÇÃO: não pode usar a função sort()'''

import random

# preencher primeira lista com números aleatórios
numeros = int(input('Quantos números deseja colocar na lista? '))
lista = []
number = 0

for i in range(numeros):
    number = random.randint(1,99)
    if number not in lista:
        lista.append(number)
        
print(lista)

# Ordenando a lista
aux = 0

for x in range(len(lista)):
    for y in range(len(lista)):
        if lista[x] < lista[y]:
            aux = lista[y]
            lista[y] = lista[x]
            lista[x] = aux

print(lista)
        
