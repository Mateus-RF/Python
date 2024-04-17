import os
lista = []

while True:
    
    print('Selecione uma opção: ')
    comando = input('[i]nserir [a]pagar [l]istar: ').upper()

    if comando == 'I':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)

    elif comando == 'A':
        indice_int = int(input('Qual o Indice: '))
        try:
            del lista[indice_int]
            
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')

    elif comando == 'L':
        os.system('cls')
        if len(lista) == 0:
            print('Nada para listar')

        for indice, variavel in enumerate(lista):
            print(indice, variavel)

    else:
        print('Comando invalido! Tente novamente: ')

''' Resolução '''


"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')