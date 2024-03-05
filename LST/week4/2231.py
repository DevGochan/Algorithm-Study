n = int(input())
ans = 0

for i in range(1, n+1):
    num = i + sum(list(map(int,str(i))))
    if num == n:
        ans = i
        break
print(ans)