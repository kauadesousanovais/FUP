import math
while True:
    num = float(input())
    if num<=0:
        break
    quad = num**2
    cubo = num**3
    raiz = math.sqrt(num)

    print(f'{quad :.2f}')
    print(f'{cubo :.2f}')
    print(f'{raiz :.2f}')
