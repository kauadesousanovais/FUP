def eh_triangulo(a,b,c):
    return a +b >c and b+c>a and c+a>b

def tipo_triangulo(a,b,c):
    if a==b and a!=c or b==c and b!=a or c==a and b!=c:
        return 'Triangulo isosceles'
    if not a==b==c:
        return 'Triangulo escaleno'
    else:
        return 'Triangulo equilatero'


a = int(input())
b = int(input())
c = int(input())

if eh_triangulo(a,b,c):
    tipo1 = tipo_triangulo(a,b,c)
    print(tipo1)

else:
    print('Não triangulo')