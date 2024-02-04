A = int(input())
B = int(input())
C = int(input())
Mul = A * B * C
List_Mul = [int (i) for i in str(Mul)] # 각 숫자를 리스트로 변환!
Cnt = {}
for num in List_Mul :
    if num in Cnt :
        Cnt[num] += 1
    else :
        Cnt[num] = 1
for j in range(10) : # Cnt의 키에 j가 있는지 확인!
    if j in Cnt :
        print(Cnt[j])
    else :
        print(0)