def funcao(x):
    soma=0
    for i in range(1,x+1):
        soma = soma + (1/i)
    return soma

x = int(input(""))
y = funcao(x)
print(f"{y:.2f}")