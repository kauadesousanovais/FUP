num1=float(input())
operacao=str(input())
num2=float(input())
if operacao=='+':
    soma=num1+num2
    print(f'{soma :.2f}')
elif operacao=='-':
    sub=num1-num2
    print(f'{sub :.2f}')
elif operacao=='*':
    mult=num1*num2
    print(f'{mult :.2f}')
elif operacao=='/':
    if num2!=0:
        div=num1/num2
        print(f'{div :.2f}')
    else:
        print('Erro')
else:
    print('Erro')