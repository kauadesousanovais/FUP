soma = 0
numerador = 1
for i in range(1, 51):
    soma = soma + numerador / i
    numerador = numerador + 2
print(f'{soma:.10f}')