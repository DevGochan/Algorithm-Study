mob = []
cnt = 0
for i in range(10) :
    number = int(input())
    mob.append(number % 42)
unique_mob = set(mob)
for i in range(len(unique_mob)) :
    cnt += 1
print(cnt)