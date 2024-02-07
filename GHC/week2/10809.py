al_list = [-1] * 26 # 알파벳의 개수만큼 초기화
word = input()

for char in word:
    index = ord(char) - 97
    if al_list[index] == -1:
        al_list[index] = word.index(char)

output_str = ' '.join(map(str, al_list)) 
# al_list의 각 항목들을 문자열 형식으로 바꾼 후, 리스트의 값과 값 사이에 공백을 넣어서 하나의 문자열로 만들어줌

print(output_str)



# 예제 1
# word = 'baekjoon'
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

