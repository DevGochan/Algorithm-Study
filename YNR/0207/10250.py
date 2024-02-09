test = int(input()) # 테스트 케이스 입력 받기

for i in range(test):   # 테스트 케이스만큼 for문 돌리기 
    h, w, n = map(int, input().split()) # 각 호텔의 층 수(h), 각 층의 방 수(w), 몇 번쨰 손님(n) 입력받기. 
                                        # map()은 배열을 새로운 배열로 반환하기 위함. split()으로 숫자 나누기.
    floor = n % h   # n번째 손님을 층수로 나눈 나머지
    d = (n//h) + 1  # 엘리베이터에서 방까지의 거리 

    if floor == 0:
        d -= 1
        floor = h 

    print (floor * 100 + d)