quantidade = int(input())
contador = 0
maior = 0
x = quantidade
while quantidade > 0:
    num = int(input())
    if x==quantidade:
        maior = num
    if num > maior:
        maior = num
        contador = 0
    if num == maior:
        contador +=1
    quantidade -= 1
print(f"{maior}")
print(f'{contador}')