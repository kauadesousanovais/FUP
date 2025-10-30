idade = int(input())
contribuicao = int(input())
if idade>=65 or contribuicao>=30 or idade>=60 and contribuicao>=25:
    print('Pode se aposentar')
else: 
    print('Nao pode se aposentar')