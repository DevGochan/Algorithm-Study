N = int(input())
Numbers = list(map(int, input().split()))
cnt = 0
for i in Numbers :
    mob = 0
    if i > 1 :
        for j in range(2, i-1) :
            if i % j == 0 :
                mob += 1
        if mob == 0:
            cnt += 1
print(cnt)