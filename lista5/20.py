import math
def funcao(x):
    raiz=math.sqrt(x)
    if raiz%1==0:
        return True
    else:
        return False
x = float(input(""))
y = funcao(x)
print(f"{y}")