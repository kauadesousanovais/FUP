def funcao(x):
    if x<0:
        num=-1
    elif x==0:
        num=0
    else: 
        num=1
    return num

x = float(input(""))
y = funcao(x)
print(f"{y}")