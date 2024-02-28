nome = 'Mateus Ribeiro Ferreira'
altura = 1.74
peso = 75
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'\npesa {peso} quilos e seu imc é'
linha_3 = f'\n{imc:.2f}'

print(linha_1,linha_2,linha_3)
