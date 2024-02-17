numbers = [int(input()) for _ in range(9)]  # 9개의 자연수를 입력받아 리스트에 저장

max_value = max(numbers)  # 리스트에서 최댓값을 찾음
max_index = numbers.index(max_value) + 1  # 최댓값의 인덱스를 찾아서 1을 더하여 몇 번째 수인지 계산

print(max_value)  # 최댓값 출력
print(max_index)  # 최댓값의 인덱스 출력
