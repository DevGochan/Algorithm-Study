# https://www.acmicpc.net/problem/1152

# 문자 입력 받기
wrd = input('문자 입력:')
# split으로 문자열 나누기('' 안에 space든 .이든 뭐든 넣어야 error가 뜨지 않음), len으로 문자의 수 계산
wrd = len(wrd.split())
print(wrd)