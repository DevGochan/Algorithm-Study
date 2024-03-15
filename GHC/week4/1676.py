import math
count = 0
n = int(input())
n_fac = list(str(math.factorial(n)))

n_fac.reverse()

for i in (n_fac) :
    if(i != '0'):
        print(count)
        break
    count += 1