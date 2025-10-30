def funcao(x):
    prox=1
    for i in range(1,x+1):    
        for i in range(i):
            print(f'{prox}' ,end=(' '))
            prox = prox + 1
        print()

x = int(input())
funcao(x)


