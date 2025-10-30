def funcao(x1,x2):
    maior = x1
    mdc = 1
    if x2>maior:
        maior = x2
    for i in range(2,maior):
        if x1%i==0 and x2%i==0:
            mdc = i
    return mdc

x1 = int(input(""))
x2 = int(input(""))
y = funcao(x1, x2)
print(f"{y}")