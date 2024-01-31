# https://www.acmicpc.net/problem/2884 

H, M = map(int,input().split()) # H는 시간 M는 분. map()함수를 통해 배열을 새로운 배열로 반환. 시간과 분 입력 받고 split()으로 문자열 나누기.

if M >= 45 :    # 만약 45분이거나 이하라면
    print(H, M-45) 
elif H > 0 and M < 45 : # 만약 0시 이상이고 45분 이하라면
    print(H-1,M+15)
else:
    print(23, M+15)