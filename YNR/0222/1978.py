# https://www.acmicpc.net/problem/1978
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

n = int(input())
number = map(int, input().split()) # map()함수로 숫자를 나열 
prime = 0   # 소수를 0으로 초기화 
for num in number:
    error = 0   # 나누었을 때 0이 되면 안되기 때문에 에러를 따로 설정해줌, 에러를 0으로 초기화 
    if num > 1 :    # 숫자가 1 이상일 때
        for i in range(2, num):  # 2부터 n-1까지의 숫자 내에서
            if num % i == 0:    # 만약 2부터 n-1까지의 숫자를 나눈 몫이 0이면
                error += 1  # 에러 증가
        if error == 0:  # 만약 에러가 없으면
            prime += 1  # 소수 증가
print(prime)