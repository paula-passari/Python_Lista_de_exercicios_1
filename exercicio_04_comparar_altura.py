''' Humberto e Thiago têm 8 anos e são primos. Humberto tem 1,20m e Thiago tem 1,08m. Um dia, Thiago perguntou para seu pai quando ele será mais alto que Humberto. Sabendo que Humberto cresce 4cm por ano e Thiago cresce 7cm por ano, crie um algoritmo que mostre com que idade Thiago será mais alto que Humberto. '''

alturaHumberto = 1.20
alturaThiago = 1.08
crecimentoHumberto = 0.04
crescimentoThiago = 0.07
idade = 8

while round(alturaHumberto, 2) >= round(alturaThiago, 2):  # usa-se o round para arredondar as casas decimais na hora da comparação
    alturaHumberto += crecimentoHumberto
    alturaThiago += crescimentoThiago
    idade += 1
    
print(f'Com {idade} anos, Thiago terá {alturaThiago:.2f}m e Humberto terá {alturaHumberto:.2f}. Com isso, Thiago será mais alto que seu primo.')