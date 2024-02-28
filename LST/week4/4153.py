Answer = []
while True :
    nums = list(map(int, input().split()))
    if sum(nums) == 0 :
        break
    maxnum = max(nums)
    nums.remove(maxnum)
    if (nums[0]**2 + nums[1]**2) == maxnum**2 :
        Answer.append("right")
    else :
        Answer.append("wrong")
for i in range(len(Answer)) :
    print(Answer[i])