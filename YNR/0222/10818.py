# https://www.acmicpc.net/problem/10818
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오. N의 정수를 공백으로 구분해서 주어짐.

N = int(input())    # 몇개 입력 받을건지
num = list(map(int, input()).split())   # 숫자를 입력 받음. split()을 통해 공백으로 구분, map()을 통해 점수를 list화
print(min(num), max(num))   # 최소와 최대 출력 