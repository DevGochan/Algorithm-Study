def decompose(n):
    # 자연수 n과 각 자리수의 합을 계산하여 반환
    return n + sum(int(digit) for digit in str(n))

# 가장 작은 생성자를 찾는 함수 
def find(n):
    # 1부터 n까지 숫자를 읽고 생성자를 찾음 
    for m in range(1, n+1): 
        # 분해합이 n과 같은 경우, m은 n의 생성자 
        if decompose(m) == n:
            return m
    return 0 # 생성자를 찾지 못하면 함수 종료 

n = int(input(""))
result = find(n)

if result:  # result가 참이면 if문 실행 거짓이면 else문 실행 됨 
    print(result)
else:
    print('0')