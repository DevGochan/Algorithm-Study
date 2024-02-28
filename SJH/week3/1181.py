N = int(input())  
words = set()     

for i in range(N):
    word = input().strip()  
    words.add(word)         

sortedWords = sorted(words, key=lambda x: (len(x), x))

for word in sortedWords:
    print(word)
