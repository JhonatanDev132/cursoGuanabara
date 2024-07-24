from math import sqrt

## Caso você queira importar alguma biblioteca do python você precisa chamar dessa maneira.

# import math 

# Quando você importa dessa maneira você irá importar todas as funcionalidades da biblioteca 
# Caso você queira chamar somente uma funcionalidade você pode chamar da seguinte maneira.

# from math import sqrt

# Assim você chama somente uma funcionalidade, no caso chamamos sqrt que significa square root(raíz quadrada), ela faz a raiz quadrada de um número que você der.

## EXEMPLO



num = int(input("Insira um número: "))
raiz = sqrt(num)

print("A raiz de {} é igual a {:.2f}.".format(num, raiz))

## Usando sem importar a biblioteca toda, quando usado dessa maneira não precisa chamar o "math".