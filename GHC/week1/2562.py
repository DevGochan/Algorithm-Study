numStr = ""  # 입력받은 숫자들 저장할 배열
index = 0  # 최댓값의 위치 기억할 변수
maxNum = 0  # 최댓값 기억할 변수

for i in range(9):
    userInput = int(input())
    numStr += str(userInput)  # str함수 => 원본유지, new객체 반환

    if maxNum < userInput:
        maxNum = userInput
        index = i + 1

print(maxNum)
print(index)
