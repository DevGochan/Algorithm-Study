n = int(input())
score = 0

nums = map(int,(input().split()))

for num in nums :
    comNum = 0
    if num > 1:
        for i in range(2, num) :
            if num % i == 0:
                comNum += 1
        if comNum == 0:
            score += 1
            
print(score)            