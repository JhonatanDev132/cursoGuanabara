import math

an = float(input("Digite o angulo que você deseja: "))
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))

print("O cosseno do ângulo {} é: {:.2f}".format(an, cos))
print("O seno do ângulo {} é: {:.2f}".format(an, seno))
print("A tangente do ângulo {} é: {:.2f}".format(an, tan))
