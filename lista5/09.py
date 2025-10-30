num1 = int(input())
num2 = int(input())
num3 = int(input())

maior = 0 
intermediario = 0
menor = 0

if num1 < num2:
    if num1 < num3:
        if num2 < num3:
            menor = num1
            intermediario = num2
            maior = num3
        else:
            menor = num1
            intermediario = num3
            maior = num2

if num2 < num1:
    if num2 < num3:
        if num1 < num3:
            menor = num2
            intermediario = num1
            maior = num3
        else:
            menor = num2
            intermediario = num3
            maior = num1

if num3 < num1:
    if num3 < num2:
        if num1 < num2:
            menor = num3
            intermediario = num1
            maior = num2
        else:
            menor = num3
            intermediario = num2
            maior = num1

if num1 == num2:
    if num1 == num3:
        menor = num1
        intermediario = num2
        maior = num3

if num1 == num2:
    if num1 != num3:
        if num1 < num3:
            menor = num1
            intermediario = num2
            maior = num3
        else:
            menor = num3
            intermediario = num2
            maior = num1

if num1 == num3:
    if num1 != num2:
        if num1 < num2:
            menor = num1
            intermediario = num3
            maior = num2
        else:
            menor = num2
            intermediario = num1
            maior = num3

if num2 == num3:
    if num2 != num1:
        if num2 < num1:
            menor = num3
            intermediario = num2
            maior = num1
        else:
            menor = num1
            intermediario = num2
            maior = num3

print(f'{menor}')
print(f'{intermediario}')
print(f'{maior}')