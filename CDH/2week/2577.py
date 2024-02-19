A = int(input())
B = int(input())
C = int(input())

result = A * B * C 

digit_counts = [0] * 10 
for digit in str(result):      
    digit_counts[int(digit)] += 1                      

for count in digit_counts[0:]:
    print(count)