while True:
    sides = sorted(map(int, input().split()))
    a, b, c = sides
    
    if a == 0 and b == 0 and c == 0:
        break
    
    if a ** 2 + b ** 2 == c ** 2:
        print('right')
    else:
        print('wrong')