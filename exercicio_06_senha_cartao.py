''' Crie um algoritmo que peça para o usuário digitar a senha do cartão. O usuário terá 3 chances. Se o usuário errar a senha 3 vezes, o cartão será bloqueado. '''

senha = 195977

tentativa = 3
c = 0
while c < tentativa:
    digite = int(input('Digite a senha DE 6 dígitos: '))
    if digite == senha:
        print('PAGAMENTO EFETUADO COM SUCESSO.')
        break
    else:
        if c < 2:
            print('SENHA INCORRETA. TENTE NOVAMENTE.')
        else:
            print('SENHA INCORRETA. CARTÃO BLOQUEADO.')
    c += 1