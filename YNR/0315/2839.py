# n이 5로 나눠지는 경우 / n이 5와 3의 조합으로 담을 수 있는 경우 / n이 3으로 나눠지는 경우 / 5와 3으로 나눠지지 않을 때

n = int(input())

if n % 5 == 0:  # 5로 나눠질 때
    print(n // 5)
else:
    p = 0   # 0 봉지 초기화
    while n > 0:
        n -= 3  # n = n - 3
        p += 1  # p = p + 1
        if n % 5 == 0:  # 5키로와 3키로를 조합해서 담을 때
            p += n // 5 # p = p + n 에서 5로 정수 몫
            print(p)
            break
        elif n == 1 or n == 2:  # 나눠지지 않을 때 (n킬로그램을 만들 수 없을 때 -1 출력이 전제)
            print(-1) 
            break
        elif n == 0:    # 3으로 나눠질 때
            print(p)
            break