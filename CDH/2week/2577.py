# 변수 A, B, C에 대한 입력을 받습니다.
A = int(input())  # A에 대한 입력
B = int(input())  # B에 대한 입력
C = int(input())  # C에 대한 입력

# A, B, C를 곱하여 결과를 계산합니다.
result = A * B * C 

# 각 숫자(0부터 9까지)의 발생 횟수를 세기 위한 리스트를 초기화합니다.
digit_counts = [0] * 10 

# 결과의 문자열 표현에서 각 숫자를 반복합니다.
for digit in str(result):
    # 숫자를 정수로 변환하고 digit_counts에 해당하는 위치의 값을 증가시킵니다.
    digit_counts[int(digit)] += 1                      

# 각 숫자의 발생 횟수를 출력합니다.
for count in digit_counts[0:]:
    print(count)
