# binary search 

def solution(K, M, A):
    
    N = len(A)
    if K >= N:
        return max(A)    
    
    M = max(A)
    start, end = 0, N * M
    ans = N * M
    
    while end >= start:
        candidate = (start + end) // 2
        
        if check(A, K, M, candidate):
            ans = candidate
            end = candidate - 1
        
        # too small
        else:
            start = candidate + 1
    
    return ans
    
def check(A, K, M, candidate):
    
    if candidate < M:
        return False 
    
    tmp = 0
    chunk = 0
    
    # the last one will be processed separately
    for i in range(len(A)-1):
        tmp += A[i]
        if tmp + A[i+1] > candidate:       # overflow
            chunk += 1
            tmp = 0
    
    # the last one
    tmp += A[-1]
    chunk += 1
    
    if chunk <= K:
        return True
    else:
        return False 

A = [2, 1, 5, 1, 2, 2, 2]
K = 3
M = 5
print(solution(K, M, A))