# https://www.acmicpc.net/problem/2562

num = []    # num 리스트를 생성하기

for i in range(9):  # for문이 9번 돌아가게
    num.append(int(input('9개의 숫자 입력: '))) # append문을 활용해 num 리스트에 숫자를 하나씩 추가

print(max(num)) # 최대값을 출력
print(num.index(max(num))+1)    # 최대값의 순번을 출력. 첫 시작이 0번이기 때문에 +1을 해줌. 