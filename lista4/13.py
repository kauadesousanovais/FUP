import math
def funcao(x):
    for i in range(1):
        termo = (1/math.sqrt(5))*((((1+math.sqrt(5))/2)**x)-(((1-math.sqrt(5))/2)**x))
        termoi = int(termo)
    return termoi

x = int(input(""))
y = funcao(x)
print(f"{y:.0f}")