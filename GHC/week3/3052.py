nums = [0] * 10

for i in range(len(nums)) :
    nums[i] = int(input()) % 42

print(len(list(set(nums))))