"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Digite seu Nome: ') or "Nada"
Idade = int(input("Digite sua Idade: ")) or "Nada"

if  nome and Idade != 'Nada':
    print(f'Seu nome é {nome}')
    print(f"Seu nome invertido é {nome[::-1]}")
    print("Seu nome tem",len(nome),"letras" )
    print('A primeira letra do seu nome é',nome[0])
    print('A última letra do seu nome é',nome[-1])
    if ' ' in nome:
        print('contem espaços') 
    else:
        print('Não contem espaços')
