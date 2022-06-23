# Cria um programa que simule um menu de reserva de poltrona de cinema. O menu deverá ter as opções de visualizar as poltronas e de reservar.


cinema = [[], [], [], [], []]
for linha in range(5):
    for coluna in range(5):
        cinema[coluna].append('O')
       


def escolha():
    # menu = True
    opcao = input(''' Digite:
1 - Layout da sala
2 - Reservar poltrona
3 - Sair''')
        
        
    if opcao == '1':
        for linha in range(0,5):
            for coluna in range(0,5):
                print(f'{cinema[linha][coluna]}', ' ', end='')
            print()
        print()
        escolha()
        
    elif opcao == '2':
        fila = int(input('Digite a fila da sala: '))
        poltrona = int(input('Digite a poltrona: '))
        if cinema[fila - 1][poltrona - 1] == 'O':
            cinema[fila - 1][poltrona - 1] = 'X'
            print('Poltrona reservada com sucesso.')
        else:
            print('Poltrona já reservada. Por favor escolha outra poltrona.')
        print()
        escolha()
            
            
    elif opcao == '3':
        print('Obrigado. Volte sempre')
        
    else:
        print('Opção inválida')
        print()
        escolha()
        
escolha()