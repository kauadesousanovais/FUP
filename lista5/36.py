def funcao(x):
    cont = 0
    maior_primo = 0
    for i in range(1,x+1):
        cont = 0
        for j in range(1,i+1):
            if i % j == 0: 
                cont = cont + 1
        if cont < 3:
            if x % i == 0:
                maior_primo=i
    return maior_primo

x = int(input(""))
y = funcao(x)
print(f"{y}")