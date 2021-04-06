def solution(A):
    
    N = len(A)
    if N == 1:
        return A[0]
    
    # all neg
    if max(A) < 0:
        return max(A)
    
    tmp, ans = 0, 0
    
    for i in range(N):
        if (tmp + A[i]) >= 0:
            tmp += A[i]
        else:
            tmp = 0
        
        ans = max(ans, tmp)
    
    return ans

A = [3, 2, -6, 4, 0]
A = [1000000]
A = [-1000000, 1000000]
A = [-2, -2]
A = [-2, -3, -1]
print(solution(A))