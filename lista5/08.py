num1 = float(input()) 
num2 = float(input())

operacao = int(input())
if 4<operacao:
    print('Erro')
elif operacao<=0:
    print('Erro')

if operacao==1:
    media=(num1+num2)/2
    print(f'{media :.2f}')
elif operacao==2:
    if num1>num2:
        dif = num1-num2
        print(f'{dif :.2f}')
    else:
        dif = num2-num1
        print(f'{dif :.2f}')
elif operacao==3:
    produto = num1*num2
    print(f'{produto :.2f}')
elif operacao==4:
    if num2>0:
        div=num1/num2
        print(f'{div :.2f}')
    else:
        print('Erro')