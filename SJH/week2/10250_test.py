T = int(input())

for i in range(T):
    H = int(input())
    W = int(input())
    N = int(input())

    floor = N % H
    if floor == 0:
        floor = H

    room = (N-1)//H +1

    print(floor * 100 + room)    