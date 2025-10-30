frase = input()
tam = len(frase)
cont = 0
for i in range(tam):
    if frase[i] == "1":
        cont += 1
print(cont)