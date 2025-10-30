def funcao(x):
    nota100 = x//100
    resto100 = x%100
    nota50 = resto100//50
    resto50 = resto100%50
    nota20 = resto50//20
    resto20 = resto50%20
    nota10 = resto20//10
    resto10 = resto20%10
    nota5 = resto10//5
    resto5 = resto10%5
    nota2 = resto5//2
    resto2 = resto5%2
    nota1 = resto2//1
    resto1 = resto2%1
    return nota100, nota50, nota20, nota10, nota5, nota2, nota1

x = int(input(""))
y1,y2,y3,y4,y5,y6,y7 = funcao(x)
print(f"{y1}")
print(f"{y2}")
print(f"{y3}")
print(f"{y4}")
print(f"{y5}")
print(f"{y6}")
print(f"{y7}")