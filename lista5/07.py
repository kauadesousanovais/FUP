salario = float(input())
prestacao = float(input())
if prestacao>(salario*0.2):
    print('Emprestimo nao concedido')
else:
    print('Emprestimo concedido')