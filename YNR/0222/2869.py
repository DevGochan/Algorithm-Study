# https://www.acmicpc.net/problem/2869
# 첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.
# 높이 V, 낮에 A미터 오를 수 있음, 밤에 B미터 미끄러짐, 정상에 올라간 후엔 미끄러지지 않음

A, B, V = map(int, input().split()) # map() 함수로 A,B,V의 정보를 저장

x = (V-B)/(A-B) # x= 일수, 올라가는 횟수 x번 - 내려가는 횟수 (x-1)번 => Ax-B(x-1)=V => x = (V-B)/(A-B)
if x == int(x): # 만약 x가 나누어 떨어진다면 출력
    print(int(x))
else:   # 아니면 1일 추가
    print(int(x) + 1)
