def funcao(x1,x2,x3):
    sq = (x1**2)+(x2**2)+(x3**2)
    qs = (x1+x2+x3)**2
    return sq, qs

x1 = float(input(""))
x2 = float(input(""))
x3 = float(input(""))
y1,y2 = funcao(x1, x2, x3)
print(f"{y1:.2f}")
print(f"{y2:.2f}")