def funcao(x):
    soma=0
    for i in range(1,x+1):
        termo = (i**2+1)/(i+3)
        soma = soma + termo
    return soma

x = int(input(""))
y = funcao(x)
print(f"{y:.2f}")