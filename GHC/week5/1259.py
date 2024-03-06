
while True :
    nums = list(input())
    if nums[0] == '0' :
        break
    
    parity = True

    for i in range(len(nums)) :
        if nums[i] != nums[-i-1] :
            parity = False

    print("yes") if parity == True else print("no")