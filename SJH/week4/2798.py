N, M = map(int, input().split())
cards = list(map(int, input().split()))

closestSum = 0


for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            cardSum = cards[i] + cards[j] + cards[k]
            
            if cardSum <= M:
                closestSum = max(closestSum, cardSum)

print(closestSum)
