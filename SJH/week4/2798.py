N, M = map(int, input().split())
cards = list(map(int, input().split()))

closestSum = 0

# 세 장의 카드를 선택하는 모든 조합을 확인
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            cardSum = cards[i] + cards[j] + cards[k]
            # 합이 M을 넘지 않으면서 M에 최대한 가까운 값을 찾음
            if cardSum <= M:
                closestSum = max(closestSum, cardSum)

print(closestSum)
