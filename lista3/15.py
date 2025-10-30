def funcao(x):
    milhar= x // 1000
    centena= (x % 1000) // 100
    dezena = (x % 100) // 10
    unidade = x // 1 % 10
    return milhar, centena, dezena, unidade

x = int(input(""))
y1,y2,y3,y4 = funcao(x)
print(f"{y1:0}")
print(f"{y2:0}")
print(f"{y3:0}")
print(f"{y4:0}")