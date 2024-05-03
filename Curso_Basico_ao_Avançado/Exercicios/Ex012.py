cpf_enviado = '74682489070'
nove_digitos = cpf_enviado[:9]

contador_1 = 0
soma_1 = 0
for i in nove_digitos:
    numero = int(i)
    soma_1 = soma_1 + numero * (10 - contador_1)
    primeiro_dig = (soma_1 * 10) % 11
    primeiro_dig = primeiro_dig if primeiro_dig <= 9 else 0
    contador_1 += 1

dez_digitos = nove_digitos + str(primeiro_dig)
contador_2 = 0
soma_2 = 0
for i in dez_digitos:
    numero = int(i)
    soma_2 = soma_2 + numero * (11 - contador_2)
    segundo_dig = (soma_2 * 10) % 11
    segundo_dig = segundo_dig if segundo_dig <= 9 else 0
    contador_2 += 1

cpf_gerado = f"{nove_digitos}{primeiro_dig}{segundo_dig}"

if cpf_enviado == cpf_gerado:
    print("CPF Valido")
else:
    print('CPF Invalido')
