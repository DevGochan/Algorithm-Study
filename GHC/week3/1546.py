n = int(input())

scores = list(map(int, input().split()))

maxScore = max(scores)

sum = 0
for i in range(len(scores)):
    scores[i] = scores[i] / maxScore * 100
    sum = sum + scores[i]
print(sum/n)
