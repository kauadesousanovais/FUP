nome1 = input()
idade1 = int(input())
nome2 = nome1
idade2 = idade1

while True:
    nome = input()
    idade = int(input())
    if idade < 0:
        break
    if idade < idade2:
        idade2 = idade
        nome2 = nome
    if idade > idade1:
        idade1 = idade
        nome1 = nome
print(f"{nome2} \n{idade2} \n{nome1} \n{idade1}")