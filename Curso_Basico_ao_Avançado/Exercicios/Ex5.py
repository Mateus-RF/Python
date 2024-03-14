"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um numero inteiro: ')

if numero.isdigit():
    numero_int = int(numero)

    resto_divisao = numero_int % 2
    if resto_divisao == 0:
        print(f'O numero {numero} é par')
    else:
        print(f'O numero {numero} é impar')
else:
    print('O numero não é inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex: 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite o Horario atual: ')
horario_int = int(hora)
horario_dia = horario_int >= 0 and horario_int <= 11
horario_tarde = horario_int >= 12 and horario_int <= 17
horario_noite = horario_int >= 18 and horario_int <= 23

if horario_dia:
    print('bom dia')
elif horario_tarde:
    print('boa tarde')
else:
    print("Boa Noite")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu Nome:')
nome_curto = len(nome) <= 4
nome_normal = len(nome) >= 5 and len(nome) <= 6

if nome_curto:
    print('nome curto')
elif nome_normal:
    print('Nome Normal')
else:
    print('Nome grande')