# https://www.acmicpc.net/problem/2775

apt = [[ 0 for _ in range(15)] for _ in range(15)]
for i in range(1, 15):
    apt[0][i] = i
    apt[i][1] = 1
 
for i in range(1, 15):
    for j in range(2, 15):
        apt[i][j] = apt[i][j-1] + apt[i-1][j]
 
t = int(input())
for t in range(t):
    k = int(input())
    n = int(input())
    print(apt[k][n]) 