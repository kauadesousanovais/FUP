def funcao(x):
    ant = x - 1
    suc = x + 1
    return ant, suc

x = int(input(""))
y1,y2 = funcao(x)
print(f"{y1}")
print(f"{y2}")