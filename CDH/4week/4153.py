# 입력 받기
while True:
    # 세 변의 길이를 입력받습니다.
    a, b, c = map(int, input().split())
    
    # 입력이 모두 0인 경우 종료합니다.
    if a == 0 and b == 0 and c == 0:
        break

    # 변의 길이로 직각 삼각형인지 판별합니다.
    if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
        print("right")
    else:
        print("wrong")
