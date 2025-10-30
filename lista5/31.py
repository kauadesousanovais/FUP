n1 = int(input())
n2 = int(input())
soma = 0 
multi = 1
if n2>n1:
    for i in range(n1,n2+1):
        if i%2==0:
            soma += i
        if i%2!=0:
            multi = multi * i
else:
    for i in range(n1,n2-1,-1):
        if i%2==0:
            soma += i
        if i%2!=0:
            multi = multi * i


print(soma)
print(multi)