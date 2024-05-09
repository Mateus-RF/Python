"""   Exercícios com funções   """

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    multi = 1
    for num in args:
        multi *= num
    return multi

multiplicação = multiplica(1,2,3,4,5)
print(multiplicação)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def par_or_impar(*args):
    for num in args:
        if num % 2 == 0:
            print(f'{num} é par')
        else:
            print(f'{num} é impar')

par_or_impar(1 , 2 , 3321 ,4 )

