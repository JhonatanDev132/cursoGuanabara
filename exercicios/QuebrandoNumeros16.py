from math import trunc
numero = float(input("Digite um número float para pegarmos a porção inteira: "))

print("A porção inteira deste número é {:.0f}".format(numero, trunc(numero)))