sequence = list(map(int, input().split()))
# .split(): 문자열을 공백을 기준으로 나누어 리스트로 만드는 역할
# map(int, ..): 리스트의 각 요소를 정수로 변환 
# list(...): map() 함수의 결과를 리스트로 변환 

if sequence == sorted(sequence):    # 오름차순 정렬 
    print("ascending")

elif sequence == sorted(sequence, reverse=True):    # 내림차순 정렬 
    print("descending")

else:
    print("mixed")