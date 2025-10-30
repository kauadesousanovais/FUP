
media=0
notaf=0
for i in range (1,4):
    nota = float(input())
    if nota>10:
        print('Nota invalida')
        break
    elif nota<0:
        print('Nota invalida')
        break
    else:
        notaf+=nota
    if i==3:
        media=notaf/3
        print(f'{media :.2f}')  
    