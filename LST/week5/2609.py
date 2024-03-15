nums = list(map(int, input().split()))
M = []
m = []
for i in range(1, min(nums)) :
    if (nums[0] % i == 0) and (nums[1] % i == 0) :
        M.append(i)
print(max(M))
#최소공배수는 모르겠어요......
