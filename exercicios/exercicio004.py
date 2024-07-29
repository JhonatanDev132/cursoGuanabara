algo = input("Digite algo para sabermos o tipo primitivo: ")

print("O tipo primitivo do que você escreveu é: ", type(algo))

print("Possui só maiúsculas? ", algo.isupper())
print("Possui só minúsculas? ", algo.islower())
print("É alfanúmerico? ", algo.isalnum())
print("É alfabético? ", algo.isalpha())
print("Está capitalizada?", algo.istitle())
print("É um numero? ", algo.isnumeric())
print('É um decimal?', algo.isdecimal())