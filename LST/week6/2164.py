N = int(input())
Nnum = []
for i in range(N) :
    Nnum.append(i+1)
while True :
    if len(Nnum) == 1 :
        break
    del Nnum[0]
    Nnum.insert((len(Nnum))-1, Nnum.pop(0))
print(Nnum[0])

#이렇게하면 맞긴한데 백준은 시간초과가 나옴.......