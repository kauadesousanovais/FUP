seg = int(input(''))
hora = seg//3600 
minuto = (seg%3600)//60
segundo = seg%60
print(f'{hora:.0f}')
print(f'{minuto :.0f}')
print(f'{segundo :.0f}')