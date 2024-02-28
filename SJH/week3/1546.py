N = int(input())

n = list(map(int, input().split()))

max = max(n)
scores = [(score / max) * 100 for score in n]
average = sum(scores) / N
print(average)