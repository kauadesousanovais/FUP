def funcao(x):
    prim = x*0.46
    segu = x*0.32
    terc = x*0.22
    return prim, segu, terc

x = float(input(""))
y1,y2,y3 = funcao(x)
print(f"{y1:.2f}")
print(f"{y2:.2f}")
print(f"{y3:.2f}")
