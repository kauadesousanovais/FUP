while True:
    print('1 - Adicao')
    print('2 - Subtracao')
    print('3 - Multiplicacao')
    print('4 - Divisao')
    print('5 - Saida')
    enter = int(input())
    if enter==1:
        num1 = float(input())
        num2 = float(input())
        soma = num1+num2
        print(f'{soma:.2f}')
        continue
    elif enter==2:
        num1 = float(input())
        num2 = float(input())
        sub = num1-num2
        print(f'{sub:.2f}')
        continue
    elif enter==3:
        num1 = float(input())
        num2 = float(input())
        mult = num1*num2
        print(f'{mult:.2f}')
        continue
    elif enter==4:
        num1 = float(input())
        num2 = float(input())
        div = num1/num2
        print(f'{div:.2f}')
        continue
    elif enter==5:
        break
    else:
        print('Opcao Invalida')
        continue