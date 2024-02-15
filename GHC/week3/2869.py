# 시간초과한 답안
# a, b, v = map(int,(input().split()))
# count = 0


# if a >= v : 
#     count = 1

# while v > 0 :
#     v = v - (a - b)
#     count += 1

#     if v == a - b :
#      break

# print(count)



a,b,v = map(int,input().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1) # 삼항연산자