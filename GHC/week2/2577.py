list_ = [0] * 10 # 초기화 안해주면 index error 발생함
a = int(input())
b = int(input())
c = int(input())

str_ = str(a * b * c) # 정수를 문자열로 변환

for i in str_: # 곱셈 결과값 순회
    list_[int(i)] += 1

for i in range(10): # 출력
    print(list_[i])


# 예제 1
# 150 * 266 * 427
# 곱셈 결과값은 17,037,300
# 출력 결과값은 3 1 0 2 0 0 0 2 0 0 