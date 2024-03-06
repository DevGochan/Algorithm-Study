# https://www.acmicpc.net/problem/2675 
# 문자열 S 입력받고, 각 문자를 R번 반복, 새로운 문자열 P 만든 후 출력
# 첫번째 줄에 테스트 케이스의 개수 T, 반복 횟수 R, 문자열 S가 공백으로 구분. 

T = int(input())    # 테스트 케이스 입력 받음

for i in range(T):
    R, S = input().split() # R, S 값을 입력 받음
    R = int(R) # R을 int로 형변환
    for i in range(len(S)): # s의 길이 내에서
        print(R*S[i] ,end='') # 문자열의 인덱스 * R의 개수, end는 공백을 없애기 위해서. 
    print()