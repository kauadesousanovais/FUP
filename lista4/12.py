import math
def funcao(x1,x2):
    for i in range (0,x1+1):
        c=math.factorial(x1)/(math.factorial(x2)*math.factorial(x1-x2))
        C=int(c)
    return C

x1 = int(input(""))
x2 = int(input(""))
y = funcao(x1, x2)
print(f"{y}")