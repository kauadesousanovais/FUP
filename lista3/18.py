def funcao(x1,x2,x3,x4):
    total= x1+x2+x3
    am1 = (x1/total)*x4
    am2 = (x2/total)*x4
    am3 = (x3/total)*x4
    return am1,am2,am3

x1 = float(input(""))
x2 = float(input(""))
x3 = float(input(""))
x4 = float(input(""))
y1,y2,y3 = funcao(x1,x2,x3,x4)
print(f"{y1:.2f}")
print(f"{y2:.2f}")
print(f"{y3:.2f}")