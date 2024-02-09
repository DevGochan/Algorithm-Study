# https://www.acmicpc.net/problem/1157

# a.lower() - a를 소문자로 변환, a.upper() - a를 대문자로 변환
# 입력된 단어를 소문자로 변환
wrd = input().lower()
# list(set())을 이용해 사용된 wrd 문자를 집합 정렬, 중복 제거
wrd_list = list(set(wrd))
temp = []   # 값 임시 저장소를 비워둠

# count - 문자열 내부에서 문자열이 포함되어 있는지 계산해서 반환하는 함수
for i in wrd_list:  # wrd_list에 입력된 문자가 몇개 있는지
    count = wrd.count(i)
    temp.append(count)  # 입력된 문자를 temp에 추가 

if temp.count(max(temp)) > 1: # 같은 수의 문자(2개)가 존재할 경우 ? 출력
    print("?")
else: # 대문자로 가장 많은 문자를 출력
    print(wrd_list[(temp.index(max(temp)))].upper())