test = int(input()) # 테스트 케이스의 개수 입력 받기

for i in range(test):   # for 문으로 테스트 케이스 개수만큼 반복 
    ox = input()    # OX 입력 받기
    score = 0   # 점수 초기화
    cnt = 0 # cnt 초기화
    for j in range(len(ox)):    # len() - OX의 길이 반환 
        if ox[j] == "O":    # O가 있으면 cnt +1, score을 cnt만큼 증가시킴
            cnt += 1
            score += cnt
        elif ox[i] == "X":  # X가 있으면 cnt를 다시 0으로 초기화
            cnt = 0
    print(score)
        