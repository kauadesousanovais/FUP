def funcao(x):
    n=0
    for i in range(0,x*2,2):
        n=n+i
    return n
x = int(input(""))
y = funcao(x)
print(f"{y}")