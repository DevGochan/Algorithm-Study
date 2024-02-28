#숫자 입력받기
num1 = int(input()) # 첫번째 숫자
num2 = int(input()) # 두번째 숫자
num3 = int(input()) # 세번째 숫자
nums = list(str(num1 * num2 * num3)) # 입력받은 숫자를 str()을 이용해 문자열로 변환, list()로 묶음 [1,7,0,3,7,3,0,0]
for i in range(10): # 0~9까지의 숫자(문자열). count는 문자열만 사용 가능
    print(nums.count(str(i)))   # count를 사용해 list 안에 수가 있는지 확인하고(ex. count(0) -> 3) 그 수만큼 print