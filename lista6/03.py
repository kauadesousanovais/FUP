frase=input()
frasemaiuscula=frase.upper()
caractere=input()
cont=0
frasenova=''
tamanho=len(frase)
for i in range(tamanho):
    letra=frasemaiuscula[i]
    letraminuscula=frasemaiuscula.lower()[i]
    if letra=='A' or letra=='E' or letra=='I' or letra=='O' or letra=='U':
        frasenova+=caractere
        cont+=1
    else:
        frasenova+=letraminuscula
print(cont)
print(frasenova)

