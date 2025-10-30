from math import factorial
from math import log10
def funcao(x):
    fat= factorial(x)
    num = log10(fat)
    indice = int(num // 1)
    soma = 0
    for i in range(0, indice+1):
        n1 = fat % 10
        soma = soma + n1
        fat = fat // 10
    return soma
x= int(input(""))
y= funcao(x)
print(y)