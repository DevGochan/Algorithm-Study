while True :
    nums = list(input())
    if nums[0] == "0":
        break
    Boolean = True
    for i in range(len(nums)) :
        if nums[i] != nums[-i-1] :
            Boolean = False
    if Boolean == False :
        print("no")
    else :
        print("yes")