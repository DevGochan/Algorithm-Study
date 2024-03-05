def min_hexagon(N):
    # 예외처리: 시작점이 1인 경우 이동 거리는 1 
    if N == 1:
        return 1
    # 육각형의 층(layer) 및 최대 방 번호(max_num) 초기화 
    layer = 1
    max_num = 1
    # 주어진 숫자가 속한 층을 찾기 위해 반복문 실행 
    while True:
        max_num += 6 * layer
        # 주어진 숫자가 max_num보다 작거나 같으면 종료(berak)
        if N <= max_num:
            break
        layer += 1  # else 블록 생략 

    return layer + 1  # 중앙에서부터 시작했으므로 1을 추가해줌

# 숫자 입력
N = int(input(""))
# 이동거리 계산
result = min_hexagon(N)
# 출력 ! 
print(result)

