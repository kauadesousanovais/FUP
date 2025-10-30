numero = int(input(''))
centenas = numero // 100
dezenas = (numero // 10) % 10
unidades = numero % 10
numero_invertido = unidades * 100 + dezenas * 10 + centenas
print(f'{numero_invertido}')