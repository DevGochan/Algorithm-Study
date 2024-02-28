N = int(input())
total = 0
Ms = list(map(float, input().split()))
Max = max(Ms)
for i in range(N) :
    Ms[i] = (Ms[i]/ Max) * 100
for i in range(N) :
    total += Ms[i]
avg = total / N
print(avg)

