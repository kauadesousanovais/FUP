n = int(input())
for i in range(1, n+1):
    comeco = 1
    for k in range(1, i+1):
        print(comeco, end=" ")
        comeco = comeco * (i - k) // k
    print('\n')