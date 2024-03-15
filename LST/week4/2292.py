N = int(input())
a = 1
b = 6
M = 1
if N == 1 :
    print(M)
else:
    while True :
        a = a + b
        M += 1
        if N <= a :
            print(M)
            break
        b += 6 