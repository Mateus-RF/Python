# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor


''' AND
 entrada = input('[E]ntrar [S]air: ')
 senha_digitada = input('Senha: ')

 senha_permitida = '123456'

 if entrada == 'E' and senha_digitada == senha_permitida:
     print('Entrar')
 else:
     print('Sair')
'''
# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)
"//-----------------//--------------------------//---------------------------//----------------------------//"
''' OR
 entrada = input('[E]ntrar [S]air: ')
 senha_digitada = input('Senha: ')

 senha_permitida = '123456'

 if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
     print('Entrar')
 else:
     print('Sair')
'''
# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)
"//-----------------//--------------------------//---------------------------//----------------------------//"

""" Operador lógico "not"
 Usado para inverter expressões
 not True = False
 not False = True
 senha = input('Senha: ')
"""
print(not True)  # False
print(not False)  # True
"//-----------------//--------------------------//---------------------------//----------------------------//"

# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  M a t e u s
# -6-5-4-3-2-1
nome = 'Mateus'
#print(nome[1])
#print(nome[-5])
#print('mat' in nome)
#print('zero' in nome)
# print(10 * '-')
# print('Mat' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
"//-----------------//--------------------------//---------------------------//----------------------------//"

"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))