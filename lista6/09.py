def funcao(x1,x2):
    maior = x1
    mmc=0
    if x2>maior:
        maior=x2
    for i in range(1,maior+1):
       if x1%i==0 and x2%i==0:
            mmc = i
    return mmc

x1 = int(input(""))
x2 = int(input(""))
y = funcao(x1, x2)
print(f"{y}")