def count_zero(n):
    count = 0
    while n > 0:
        n //= 5 # 5의 배수가 0을 만들어냄 
        count += n
    return count

# 정수 N 입력 
N = int(input(""))

# 출력 
print(count_zero(N))