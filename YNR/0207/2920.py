nums = list(map(int, input().split()))  # nums에 list()로 숫자들을 입력받기. map()은 배열을 새로운 배열로 반환하기 위함. split()으로 숫자 나누기.

if nums == sorted(nums):    # defalut. sort 오름차순 정렬
    print ("ascending")
elif nums == sorted(nums, reverse = True): # reverse sort, True 내림차순 정렬
    print ("descending")
else:
    print("mixed")