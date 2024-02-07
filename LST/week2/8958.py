n = int(input())
score_list = []
for i in range(n):
    ox = input()
    score = 0
    cnt = 0
    for j in range(len(ox)) :
        if ox[j] == 'O' :
            cnt += 1 
            score += cnt # O가 연속으로 있을경우
        else :
            cnt = 0 # X가 나올경우
    score_list.append(score) # 각각의 점수를 저장할 리스트 생성
for i in score_list :
    print(i)

        

    
    
