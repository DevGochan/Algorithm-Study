# https://www.acmicpc.net/problem/3052
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

num = list()    # 숫자를 저장할 리스트 생성
for i in range(10):
    numbers = int(input())    # 숫자 10개 입력 받음
    num.append(numbers % 42)  # num에 나누기 42를 추가함. append() 파이썬 리스트 끝에 새로운 요소를 추가하는 메소드. 
num = set(num)  # set()함수를 통해 자료형(list)에 있는 숫자를 집합으로 변환 
print(len(num)) # num에 속한 값의 개수를 반환 