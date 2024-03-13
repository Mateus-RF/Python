a = 'AAAAA'
b = 'BBBBBB'
c = 1.1

# string com parmentro nomeado
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format( nome1=a, nome2=b, nome3=c )

# string sem parametro nomeado
text = 'a={} b={} c={:.2f}'
formato_2 = text.format(a, b, c)

print(formato)
print(formato_2)