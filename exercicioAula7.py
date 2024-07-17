import math

# n = int(input("Digite um número: "))
#sucessor = n+1
#antecessor = n-1
#dobro = n*2
#triplo = n*3
#raiz = math.pow(n, 1/2)

#print("O número inteiro é {}, o seu antecessor é {} e o seu sucessor é {}.".format(n, antecessor, sucessor))
#print("O seu dobro é {}, o triplo é {} e a raiz é {}.".format(dobro, triplo, raiz))

#nota1 = float(input("Digite a primeira nota: "))
#nota2 = float(input("Digite a segunda nota: "))

#media = (nota1 + nota2) / 2

#print("A média do aluno é: {}".format(media))

medida = float(input("Digite uma medida em metros: "))
cm = medida * 100
mm = medida * 1000

print("A medida de {}m corresponde a {:.0f}cm e {:.0f}mm".format(medida, cm, mm))