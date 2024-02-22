n = int(input())
ary = [0] * n

ary = list(map(int, input().split()))

print(min(ary), end = ' ')
print(max(ary))


