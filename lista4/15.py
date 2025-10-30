import math
def funcao(x):
    soma=0
    for i in range(x+1):
        soma=soma +(1/math.factorial(i))
    return soma

x = int(input(""))
y = funcao(x)
print(f"{y:.8f}")