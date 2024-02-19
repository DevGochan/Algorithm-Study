T = int(input())
rooms = []

for _ in range(T):
    H, W, N = map(int, input().split())
    
    floor = N % H  # 손님이 머무는 층
    room_number = N // H + 1  # 손님이 머무는 층의 방 번호
    
    # 만약 N이 H의 배수라면 맨 꼭대기 층에 배정
    if floor == 0:
        floor = H
        room_number -= 1
    
    # 결과 저장
    rooms.append(floor * 100 + room_number)

# 모든 방 번호 출력
for room in rooms:
    print(room)