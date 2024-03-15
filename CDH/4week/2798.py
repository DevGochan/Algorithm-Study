def find_nearest_sum(cards, target):
    cards.sort()  # 카드를 오름차순으로 정렬합니다.
    n = len(cards)  # 카드의 개수를 저장합니다.
    nearest_sum = 0  # 가장 가까운 합을 저장할 변수를 초기화합니다.

    for i in range(n - 2):  # 첫 번째 카드를 선택하는 루프
        left, right = i + 1, n - 1  # 현재 카드의 오른쪽 끝과 가장 오른쪽 끝을 가리킵니다.
        
        while left < right:  # 세 번째 카드를 선택하는 루프
            total = cards[i] + cards[left] + cards[right]  # 세 카드의 합을 계산합니다.
            if total <= target:  # 합이 목표값 이하인 경우
                if total > nearest_sum:  # 현재 합이 지금까지의 최대 합보다 큰 경우
                    nearest_sum = total  # 최대 합을 업데이트합니다.
                left += 1  # 왼쪽 포인터를 오른쪽으로 이동하여 합을 키웁니다.
            else:  # 합이 목표값을 넘는 경우
                right -= 1  # 오른쪽 포인터를 왼쪽으로 이동하여 합을 줄입니다.
    
    return nearest_sum  # 가장 가까운 합을 반환합니다.

# 입력 받기
N, M = map(int, input().split())  # 카드의 개수와 목표 합을 입력받습니다.
cards = list(map(int, input().split()))  # 카드에 쓰여진 수를 입력받습니다.

# 최대 합 출력
print(find_nearest_sum(cards, M))  # 주어진 카드와 목표 합을 이용하여 최대 합을 계산하고 출력합니다.
