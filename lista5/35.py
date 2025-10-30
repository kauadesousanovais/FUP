for i in range(1000,10000):
    milhar = i//100
    dezena = i%100
    soma = milhar+dezena
    perfeito = soma**2
    if perfeito==i:
        print(i)
    