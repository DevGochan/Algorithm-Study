from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())
q = deque([i for i in range(1, n+1)])

while (len(q) != 1):
    q.popleft()
    if len(q) == 1:
        break
    else:
        q.append(q.popleft())   # 맨 왼쪽 원소를 맨 오른쪽으로 옮김 

print(q[0])