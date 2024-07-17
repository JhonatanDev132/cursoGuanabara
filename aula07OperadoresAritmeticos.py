# Ordem de Precedência

# 1. () Parenteses

# 2. ** Potenciação // 5**2 = 25

# 3. // Divisão inteira // 5//2 = 2
#    % Resto de divisão // 5%2 = 1
#    * Multiplicação // 5*2 = 10
#    / divisão // 5/2 = 2.5

# 4. + Adição // 5+2 = 7
#    - Subtração // 5-2 = 3

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro: "))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

print("A soma é {}, a multiplicação é {}, e a divisão é {:.3f} ".format(s, m, d))
print("Divisão inteira {}, e potência {}".format(di, e))