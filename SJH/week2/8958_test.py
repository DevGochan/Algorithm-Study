testCount = int(input())

for i in range(testCount):
    result = input()
    score = 0
    combo = 0
    for j in result:
     if j == 'O':
        combo += 1
        score += combo 
     else :
        combo =0

    print(score)         

