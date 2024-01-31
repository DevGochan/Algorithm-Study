list_ = [0] * 10 # 초기화 안해주면 index error 발생함
a = int(input())
b = int(input())
c = int(input())

str_ = str(a * b * c) # 정수를 문자열로 변환

for i in str_:
    list_[int(i)] += 1

for i in range(10):
    print(list_[i])