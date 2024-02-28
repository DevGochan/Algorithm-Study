test = int(input()) # 테스트 케이스 입력 받기

for i in range(test):   # 테스트 케이스만큼 for문 돌리기 
    h = int(input())
    w = int(input())
    n = int(input())

    floor = n % h   # n번째 손님을 층수로 나눈 나머지
    d = (n//h) + 1  # 엘리베이터에서 방까지의 거리 

    if floor == 0:
        d -= 1
        floor = h 

    print (floor * 100 + d)