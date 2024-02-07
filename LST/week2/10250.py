T = int(input())
RoomNumber_list = []
for i in range(T) :
    H, W, N = map(int, input().split())
    F = N % H
    D = N / H + 1
    if F == 0:
        D -= 1
        F = H
    RoomNumber = int(F * 100 + D)
    RoomNumber_list.append(RoomNumber)
    RoomNumber = 0

for i in range(T) :
    print(RoomNumber_list[i])