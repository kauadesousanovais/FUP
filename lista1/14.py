num = int(input(''))
unidades = num // 1 % 10
dezenas = num // 10 % 10
centenas = num // 100 % 10
milhares = num // 1000 % 10
print(f'{milhares}')
print(f'{centenas}')
print(f'{dezenas}')
print(f'{unidades}')