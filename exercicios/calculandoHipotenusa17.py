from math import hypot

oposto = float(input("Qual a medida do seu cateto oposto? "))
adjacente = float(input("E a do adjacente? "))
hy = hypot(oposto, adjacente)

print("A hipotenusa vai medir {:.2f}".format(hy))