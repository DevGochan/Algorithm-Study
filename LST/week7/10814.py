import sys
N = int(sys.stdin.readline())
Names = []
for i in range(N):
    a = sys.stdin.readline().split()
    Names.append(a)
for i in sorted(Names, key = lambda x : x[0]):
    print(i[0], i[1])