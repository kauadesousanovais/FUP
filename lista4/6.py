def funcao(x):
    n = 0
    for i in range(1,x+1):
        n = n + i
    return n

x = int(input(""))
y = funcao(x)
print(f"{y}")