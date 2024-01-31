string = input().upper()  # 문자열을 대문자로 변경해줌

string_set = list(set(string))  # set함수로 중복 제거 후 다시 list로 만들어줌

cnt = []  # 입력받은 문자열의 알파벳 개수를 기억할 변수

for i in string_set:
    cnt.append(string.count(i))  # count는 문자열에서 i(변수)의 총 개수를 반환

if cnt.count(max(cnt)) > 1:  # cnt내의 최대값이 2 이상일 때
    print("?")

else:
    print(string_set[cnt.index(max(cnt))])



# Mississipi -> MISSISSIPI -> MISP
# cnt = 1, 4, 4, 1
    
# zZa -> ZZA -> ZA
# cnt = 2, 1