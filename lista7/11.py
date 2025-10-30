def mdc(x1,x2 ):
    if x2 == 0:
        return x1
    return mdc(x2, x1 % x2)