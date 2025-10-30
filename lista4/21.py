def funcao(x):
    for i in range(x):
        pintudo = 2*i + 1
        branco = x - 1-i
        print(' '*branco + '*'*pintudo)

x = int(input(""))
funcao(x)