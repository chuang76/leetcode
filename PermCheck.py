def solution(A):
    table = [0] * 100000
    N = len(A)
    
    for i in range(len(A)):
        
        if A[i] > 100000:
            return 0
        
        if table[A[i]-1] != 0:
            return 0
        else:
            table[A[i]-1] = A[i]       
    
    total = (N * (N + 1)) // 2 
    if sum(table) == total:
        return 1

    return 0

A = [1000000000]   # 0
A = [4, 1, 3, 2]   # 1
A = [4, 1, 3]      # 0 
print(solution(A))          