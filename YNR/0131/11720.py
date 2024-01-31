# https://www.acmicpc.net/problem/11720

num = input()   # 숫자의 개수를 입력받기
nums = list(map(int,input()))   # nums에 list()로 숫자들을 입력받기. map()은 배열을 새로운 배열로 반환하기 위함.

print(sum(nums))    # sum()을 통해 nums의 합을 구하고 출력.