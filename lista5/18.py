def funcao(x):
    dia = x[0:2]
    mes = x[3:5]
    ano = x[6:]
    dia = int(dia)
    mes = int(mes)
    if dia<0:
        print('Data invalida')
    elif dia>30:
        print('Data invalida')
    if mes==1:
        mes='janeiro'
    elif mes==2:
        if dia<=28:
            mes='fevereiro'
    elif mes==3:
        mes='marco'
    elif mes==4:
        mes='abril'
    elif mes==5:
        mes='maio'
    elif mes==6:
        mes='junho'
    elif mes==7:
        mes='julho'
    elif mes==8:
        mes='agosto'
    elif mes==9:
        mes='setembro'
    elif mes==10:
        mes='outubro'
    elif mes==11:
        mes='novembro'
    elif mes==12:
        mes='dezembro'   
    else:
        print('Data invalida')        
    
    return f'{dia} de {mes} de {ano}'
            

x = input("")
y = funcao(x)
print(f"{y}")