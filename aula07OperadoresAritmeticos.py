# Ordem de Precedência

# 1. () Parenteses

# 2. ** Potenciação // 5**2 = 25

# 3. // Divisão inteira // 5//2 = 2
#    % Resto de divisão // 5%2 = 1
#    * Multiplicação // 5*2 = 10
#    / divisão // 5/2 = 2.5

# 4. + Adição // 5+2 = 7
#    - Subtração // 5-2 = 3

#n1 = int(input("Digite um número: "))
#n2 = int(input("Digite outro: "))
##s = n1+n2
#m = n1*n2
#d = n1/n2
#di = n1//n2
#e = n1**n2

#print("A soma é {}, a multiplicação é {}, e a divisão é {:.3f} ".format(s, m, d))
#print("Divisão inteira {}, e potência {}".format(di, e))

#numero = int(input("Digite um número para que a tabuada seja feita: "))
#contador = 0

#print("A tabuada do número {} é: ".format(numero))

#while contador <= 10 :
#    num = numero * contador
#    print("{} x {} = {}".format(numero, contador, num))
#    contador += 1


#carteira = float(input("Quanto dinheiro você tem na carteira? "))
#precoReal = 3.27

#carteiraDolar = carteira / precoReal

#print("Com R${:.2f} Você pode comprar ${:.2f} doláres.".format(carteira, carteiraDolar))

largura = float(input("Escreva a largura da parede: "))
altura = float(input("Escreva a altura da parede: "))

area = largura * altura
tinta = area / 2

print("Sua parede tem uma area de {}m², e será necessário {}l de tinta para pintar ela.".format(area, tinta))
