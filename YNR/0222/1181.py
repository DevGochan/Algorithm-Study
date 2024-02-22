# https://www.acmicpc.net/problem/1181
# 단어 정렬. 알파벳 소문자로 이루어진 n개의 단어가 들어오면 > 길이가 짧은 것 부터 > 길이가 같으면 사전 순으로
# 중복된 단어는 하나만 남기고 제거 
# 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 
# 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 
# 주어지는 문자열의 길이는 50을 넘지 않는다.

n = int(input())
word = [str(input()) for i in range(n)] # 문자이기에 str로 해줌
word = list(set(word))  # set()으로 중복 단어 제거
word.sort()
word.sort(key=len)  # 길이순으로 정렬하는 메소드 
for i in word:
    print(i)