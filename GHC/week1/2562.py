index = 0  # 최댓값의 위치 기억할 변수
maxNum = 0  # 최댓값 기억할 변수

for i in range(9):
    userInput = int(input())

    if maxNum < userInput:
        maxNum = userInput
        index = i + 1

print(maxNum)
print(index)
