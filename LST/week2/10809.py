S = input()
alphas = [-1] * 26

for char_index in range(len(S)):
    char = S[char_index]
    # 현재 문자가 이미 처리된 경우 건너뜀
    if alphas[ord(char) - ord('a')] != -1:
        continue
    # 현재 문자의 인덱스를 저장, ord는 문자를 해당하는 아스키 코드값으로 변환하는 함수!
    alphas[ord(char) - ord('a')] = char_index
# 결과를 출력
print(" ".join(map(str, alphas)))

    


