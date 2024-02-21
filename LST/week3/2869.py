A, B, V = map(int, input().split())
D = 0
while True :
    if A - B == V :
        print(D)
        break
    else :
        D = (V - B) / (A - B)
        if D != int(D) :
            print(int(D) + 1)
            break
        print(int(D))
        break