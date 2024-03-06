# https://www.acmicpc.net/problem/1259

while True:
    n = input()

    if n == '0':    # 0이 될 때까지 입력 받음
        break
else:
    if n == n[::-1]:    # 입력 받은 수를 거꾸로 뒤집었을 때 사용함
        print("yes")
    else:
        print("no")
    