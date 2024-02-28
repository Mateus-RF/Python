#operadores aritmeticos
# Ordem de precedencia: 
#   1º () -> parenteses
#   2º ** -> exponenciação
#   3º * | / | // | % -> multiplicação, Divisão, Divisão inteira, Resto da divisão
#   4º + | - -> Soma, Subtração
'''
import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz do numero é {}'.format(math.floor(raiz)))
print('A raiz do numero é {}'.format(math.ceil(raiz)))
print('A raiz do numero é {}'.format(raiz))
'''

'''
frase = "curso em video python"
print(frase[9:21:2])
print(frase[:14])
print(frase[15:])
print(frase[9::3])
'''
'''frase = "Curso em Video Python"
# Mostra a quantidades de caracteris.
print(len(frase))

# Mostra quantas vezes a letra "o".
print(frase.count('o'))

# Mostra quantas vezes a letra "o" aparece entre 0 e 13.
print(frase.count("o",0, 13))

# Mostra aonde começa a frase "deo".
print(frase.find("deo"))

# Mostra que não existe a palavra 'android' com o sombolo -1.
print(frase.find('android'))

# Mostra que existe a palavra dentro da frase. OBS: depende se for MAIUSCULA OU MINUSCULA.
print('curso'in frase)
print('Curso'in frase)

# Troca a palavra caso exista na frase ex:"python". por outra palavra ex:"Android". OBS: depende se for MAIUSCULA OU MINUSCULA.
print(frase.replace('Python', 'Android'))

# Coloca toda a frase em letras maiusculas.
print(frase.upper())

# Coloca toda a frase me letras minusculas.
print(frase.lower())

# Deixa apenas a primera letra da frase em maiscula ex:"Curso em video python".
print(frase.capitalize())

# Deixa todas as primeiras letras da palavras maiuscula ex:"Curso Em Video Python".
print(frase.title())

# Gera uma lista com as palavras da frase ex: 'Curso de python' --> ['Curso', 'de', 'python']
print(frase.split())

lista = ['Curso', 'em', 'Video', 'python']
# Junta uma lista em uma unica frase.
print(' '.join(lista))
'------------------------------------------------------------------------------------------------------------------'
frase2 = "   Aprenda Python  "
# Retira todos os espaços inuteis nas frases.
print(frase2.strip())

# Remove apenas os espaços da direita
print(frase2.rstrip())

# Remove apenas os espaços da esquerda
print(frase2.lstrip())
'''