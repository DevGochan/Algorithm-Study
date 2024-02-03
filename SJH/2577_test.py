A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)
count = [0] * 10
print(result)

for i in result:
    count[int(i)] += 1

for j in count:
    print(j)