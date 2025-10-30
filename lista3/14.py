def funcao(x):
    # pegar o valor das centenas
    centenas = x // 100
    # pegar o valor das dezenas 
    dezenas = (x // 10) % 10
    # pegar unidades 
    unidades = x % 10
    numinv = unidades * 100 + dezenas * 10 + centenas
    return numinv

x = int(input(""))
y = funcao(x)
print(f"{y:0}")
