n = int(input())
if n%3==0 or n%5==0:
    if n%15==0:
        print(False)
    else:
        print(True)
    