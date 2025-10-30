import math
def funcao(x):
    for i in range(0,x+1):
        n= math.factorial(i)
    return n

x = int(input(""))
y = funcao(x)
print(f"{y}")