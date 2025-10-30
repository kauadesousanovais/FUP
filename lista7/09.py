def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)
def sf(n):
    if n == 1:  
        return 1
    return fatorial(n) * sf(n - 1)