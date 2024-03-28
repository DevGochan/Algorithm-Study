# https://www.acmicpc.net/problem/1546
# 점수 최댓값 M, 모든 점수를 점수/M*100으로 고침
# ex) 최고점 70, 수학점수 50 -> 수학 점수 50/70*100=71.43점
# 새로운 평균을 구하는 프로그램 작성

subject = int(input())
scores = list(map(int, input().split())) # map()함수로 점수를 list화 
M = max(scores)
for i in range(subject):
    scores[i] = scores[i] / M * 100
    sum = sum + scores[i]

print(sum(scores)/subject)