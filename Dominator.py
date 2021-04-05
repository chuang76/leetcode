def solution(A):
    
    N = len(A)
    if N == 0:
        return -1 
    
    tmp = A[:]               # copy 
    leader = -1
    A.sort()
    
    count = 0
    ans = 0
    candidate = A[N // 2] 
    for i in range(N):
        if tmp[i] == candidate:
            count += 1
            ans = i
    
    if count > (N // 2):
        return ans
    
    return -1 

A = [3, 4, 3, 2, 3, -1, 3, 3]
A = [-1, -2, -2, -2, 1]
A = [-2147483648, 2147483647]
A = [0, 0]
A = []
print(solution(A))