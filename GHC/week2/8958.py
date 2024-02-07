n = int(input()) # 테스트 케이스 횟수

for i in range(n):
    ox_list = input()
    score = 0       
    score_sum = 0

    for ox in ox_list:
        if ox == 'O':
            score += 1
        else :
            score = 0
        score_sum += score
    print(score_sum)


# 예제
# n = 1,    ox_list = 'OOXXOXXOOO'