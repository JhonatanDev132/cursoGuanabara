n = input('Insira um número: ')

print('O tipo primitivo desse valor é: ', type(n))
print('É um número? ', n.isnumeric())
print('É um alpha?', n.isalpha())
print('É um decimal?', n.isdecimal())
print('É um caractere minúsculo?', n.islower())