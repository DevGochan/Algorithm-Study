T = int(input()) 

for _ in range(T):
    k = int(input()) 
    n = int(input())  

    residents = [i for i in range(1, n+1)]
  
    for _ in range(k):
        for j in range(1, n):
            residents[j] += residents[j-1]
    
    print(residents[-1]) 
