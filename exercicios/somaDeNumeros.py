n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2

# A forma mais antigo do python
# print('A soma entre ', n1, 'e', n2, 'vale', s)

print('A soma entre {0} e {1} resulta em: {2}'.format(n1, n2, s))