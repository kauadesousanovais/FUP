def funcao(x):
    final=1
    for i in range (2,x+1):
        final = i ** final
    return final

x = int(input(""))
y = funcao(x)
print(f"{y}")
