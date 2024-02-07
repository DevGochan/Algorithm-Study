# n // h + 1 을 통해 방번호 도출
# if문 이용하여 n % h == 0 이면 n // h 를 통해 호수가 되고 a는 층이 됨
# floor에 100을 곱하고 num을 더하면 방번호 출력

# https://ywtechit.tistory.com/91


T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    num = N // H + 1
    floor = N % H
    if N % H == 0:
        num = N // H
        floor = H
    print(f'{floor * 100 + num}')

#  https://ooyoung.tistory.com/88