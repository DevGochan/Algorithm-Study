P = [-1] * 26

word = input()
# enumerate(word): word 문자열을 순회하면서 각 문자와 인덱스를 생성
for idx, char in enumerate(word):
    # ord(): 주어진 문자의 유니코드 포인트를 반환한다. 알파벳의 순서를 계산하기 위해 사용 
    # 'a': 알파벳 'a'의 유니코드 코드 포인트를 나타냄 
    if P[ord(char) - ord('a')] == -1:
        P[ord(char) - ord('a')] = idx

for pos in P:
    print(pos, end = ' ')
