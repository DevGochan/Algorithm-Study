N, M = map(int, input.split())
sum = []
nums = list(map(int, input.split()))
for i in range(len(nums)-2) :
    for j in range(i+1, len(nums)-1) :
        for z in range(j+1, len(nums)) :
            Msum = nums[i] + nums[j] + num[z]
            if sum > M :
                continue
            else :
                sum.append(Msum)
print(max(sum))
