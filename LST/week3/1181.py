N = int(input())
word = []
for i in range(N) :
    word.append(input())
word = list(set(word))
word.sort()
word.sort(key = len)
for i in word :
    print(i)