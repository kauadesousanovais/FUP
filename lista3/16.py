def funcao(x):
    hora = x // 3600
    minuto = (x % 3600) // 60 
    seg = x % 60
    return hora, minuto, seg

x = int(input(""))
y1,y2,y3 = funcao(x)
print(f"{y1}")
print(f"{y2}")
print(f"{y3}")