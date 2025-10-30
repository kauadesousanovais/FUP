def funcao(x1,x2):
    if x1>x2:
        maior=x1
    else: 
        maior=x2
    return maior

x1 = float(input(""))
x2 = float(input(""))
y = funcao(x1, x2)
print(f"{y:.2f}")