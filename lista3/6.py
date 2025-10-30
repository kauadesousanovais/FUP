import math
def funcao(x):
    v = 4/3*math.pi*(x**3)
    a = 4*math.pi*(x**2)
    return v, a

x = float(input(""))
y1,y2 = funcao(x)
print(f"{y1:.2f}")
print(f"{y2:.2f}")