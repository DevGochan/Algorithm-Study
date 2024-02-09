n = int(input())
word = [''] * n

for i in range(n):
    word[i] = input()

# 중복 제거
noDupList = list(set(word))


# 정렬
noDupList.sort()
noDupList.sort(key=len) # 요소의 길이를 기준으로 오름차순 정렬

for i in range(len(noDupList)):
    print(noDupList[i])