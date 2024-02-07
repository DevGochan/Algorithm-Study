N = int(input())  # 숫자의 개수 N을 입력받음
numbers = input()  # N개의 숫자를 공백 없이 입력받음

# 입력받은 숫자를 각 자리마다 분리하고 합을 계산
total = sum(int(digit) for digit in numbers)

print(total)
