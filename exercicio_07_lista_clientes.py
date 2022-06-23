''' Faça um algoritmo que cadastre os nomes de clientes em uma lista. Crie também uma maneira de pesquisar se determinado cliente está na lista. '''

# cadastrar clientes
clientes = []
num_clientes = int(input('Digite o número de clientes que deseja cadastrar: '))

for i in range(num_clientes):
    nome = input(f'Digite o nome do {i+1}º cliente: ')
    clientes.append(nome.capitalize())

    
# buscar clientes
busca = input('Digite o nome que deseja buscar: ')
if busca.capitalize() in clientes:
    print(f'Cliente {busca.capitalize()} está cadastrado no banco de dados.')
else:
    print(f'Cliente {busca.capitalize()} não está cadastrado no banco de dados.')
