import math
def funcao(x1,x2):
    soma=0
    for i in range (0,x2+1):
        taylor=((-1)**i)*(x1**(2*i+1))
        deno= math.factorial((2*i+1))
        soma = soma + (taylor/deno)
    return soma
    
x1 = float(input(""))
x2 = int(input(""))
y = funcao(x1, x2)
print(f"{y:.8f}")