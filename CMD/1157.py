word = input().upper()  # 입력 받은 단어를 대문자로 변환
char_count = {}  # 알파벳 개수를 저장할 딕셔너리

for char in word:
    if char.isalpha():  # 알파벳인 경우에만 처리
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

max_count = max(char_count.values())  # 가장 많이 사용된 알파벳의 개수

# 가장 많이 사용된 알파벳들을 찾음
most_used_chars = [char for char, count in char_count.items() if count == max_count]

if len(most_used_chars) == 1:
    print(most_used_chars[0])
else:
    print("?")
