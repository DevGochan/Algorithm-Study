userInput = input()
numbers = userInput.split()  # 공백 기준으로 숫자 분리

# str -> int
H = int(numbers[0])
M = int(numbers[1])

M = M - 45

if M < 0:
    H -= 1
    M = M + 60

if H < 0:
    H = 23

print(H, M)
