#palavra=str(input())

#print()

x = str(input())
x = x.split()
x = ' '.join(x)
quant = len(x)
for i in range(0, quant, 1):
    numero = ord(x[i])
    numero+=1
    letra = chr(numero)
    print(letra, end='')
    
