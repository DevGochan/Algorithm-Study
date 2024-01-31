list_ = [0] * 10
a = int(input())
b = int(input())
c = int(input())

str_ = str(a * b * c)

for i in str_:
    list_[int(i)] += 1

for i in range(10):
    print(list_[i])