def funcao(x):
    if len(x) == 10 and x[2] == '/' and x[5] == '/' and x[:2].isdigit() and x[3:5].isdigit() and x[6:].isdigit():
        dia = int(x[:2])
        mes = int(x[3:5])
        ano = int(x[6:])
        return dia,mes,ano
    else:
        return 0,0,0
x = input("")
y1, y2, y3 = funcao(x)
print(f"{y1}")
print(f"{y2}")
print(f"{y3}")