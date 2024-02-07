T = int(input())

# 테스트 케이스의 개수만큼 퀴즈 결과를 입력 받음
quiz_results = [input() for _ in range(T)]

# 각 테스트 케이스마다 점수 계산하여 출력
for result in quiz_results:
    score = 0            # 점수 초기화 
    zero_sum = 0         # 연속된 0의 개수 저장할 변수 

    for answer in result:
        if answer == 'O':
            zero_sum += 1
            score += zero_sum
        else:
            zero_sum = 0   # X를 만나면 연속된 0의 개수 초기화 
    
    print(score)  # 각 테스트 케이스마다 점수 출력
