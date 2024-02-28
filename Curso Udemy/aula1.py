"""
DocStrings

Um docstring é um literal de cadeia de caracteres especificado no código-fonte que é usado,
como um comentário, para documentar um segmento específico de código.

Obs: DocString Não é considerado um comentario

"""

''' Usar para escrever suas notas '''

'---------------------------------------------------------------------------------------------------------'

# Comentarios
#
# Comentário simples em Python basta colocar uma hashtag(#) antes do texto.
#
# Tudo que aparecer após uma hashtag(#) será ignorado, porém, 
# você pode colocar código na mesma linha(desde que antes de iniciar o comentário)
# que esse será executado


print(123) # Na frente
# Abaixo
print(456)
'---------------------------------------------------------------------------------------------------------'

# String -> str
# É um conjunto de caracteres dispostos numa determinada ordem, geralmente utilizada para representar palavras, frases ou textos.
nome = 'Mateus'
profissao = 'Estudante ADS-IFCE'

print(type(profissao))
print(type(nome))

# Inteiro -> int
# O tipo inteiro é um tipo composto por caracteres numéricos (algarismos) inteiros.
# É um tipo usado para um número que pode ser escrito sem um componente decimal, podendo ter ou não sinal, isto é: ser positivo ou negativo.
idade = 18
ano = 2005

print(type(idade))
print(type(ano))

# Ponto flutuante -> float
#É um tipo composto por caracteres numéricos (algarismo) decimais.

# Ponto flutuante é um tipo usado para números racionais (números que podem ser representados por uma fração) 
# informalmente conhecido como “número quebrado”.

altura = 1.80
peso = 73.55

print(type(peso))
print(type(altura))

# Boolean -> bool
#Tipo de dado lógico que pode assumir apenas dois valores: falso ou verdadeiro (False ou True em Python).

#Na lógica computacional, podem ser considerados como 0 ou 1.
fim_de_semana = True
feriado = False

print(type(fim_de_semana))
print(type(feriado))