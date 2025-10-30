def funcao(x):
    if x==0:
        return 0
    else:
        return x**3 + funcao(x-1)