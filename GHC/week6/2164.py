# 시간초과 난 답안 (출력 결과는 잘 나옴)
# import sys
# input = sys.stdin.readline

# n = int(input())

# card = []

# for i in range(n) :
#     card.append(i + 1)

# while len(card) != 1 :
#     del card[0]
#     temp = card[0]
#     del card[0]
#     card.append(temp)

# print(card[0])


import sys
from collections import deque

n = int(sys.stdin.readline())
card = deque()

for i in range(1, n+1):
    card.append(i)
    
while len(card) > 1:
    card.popleft()
    card.append(card.popleft())

print(card[0])