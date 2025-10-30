frase=input()
frasemaiuscula=frase.upper()
cont=0
frasenova=''
tamanho=len(frase)
for i in range(tamanho):
    letra=frasemaiuscula[i]
    letraoriginal=frase[i]
    if letra=='A' or letra=='E' or letra=='I' or letra=='O' or letra=='U':
        frasenova+=''
        cont+=1
    else:
        frasenova+=letraoriginal
print(frasenova)