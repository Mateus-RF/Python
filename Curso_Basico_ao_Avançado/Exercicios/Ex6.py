nome = 'Mateus Ribeiro'
tamanho_nome = len(nome)
contador = 0
nome_mod = ''
while contador < tamanho_nome:
    letra = nome[contador]
    nome_mod += f'*{letra}'
    contador += 1
nome_mod += "*"

print(nome_mod)