from math import gcd  # gcd é a função para calcular o maior divisor comum

def simplificada(numerador, denominador):
    # Verifica se o denominador é zero
    if denominador == 0:
        return "Denominador não pode ser zero."
    
    # Calcula o maior divisor comum (MDC) entre o numerador e o denominador
    divisor_comum = gcd(numerador, denominador)
    
    # Divide o numerador e o denominador pelo MDC para simplificar a fração
    numerador_simplificado = numerador // divisor_comum
    denominador_simplificado = denominador // divisor_comum
    
    # Retorna a fração simplificada
    return numerador_simplificado, denominador_simplificado