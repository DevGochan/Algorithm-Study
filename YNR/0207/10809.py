from string import ascii_lowercase  # string 모듈에서 ascii_lowercase를 import 
L = list(ascii_lowercase)   # 알파벳 리스트를 만듦. ascii_lowercase를 list에 넣음 [a-z]

S = input() # 소문자로 이루어진 단어 S 입력받기

for i in L:
    if i in S:  # 알파벳이 포함되어 있으면 숫자 출력. index()로 원하는 값의 인덱스 위치를 찾음. end = ' ' - 줄바꿈 X, 출력값에 이어서 출력함 
        print(S.index(i), end= ' ')
    else:   # 알파벳이 포함되어 있지 않으면 -1 출력
        print( -1, end =' ')