def solution(A):
    
    if len(A) < 2:
        return 0
    
    ans = 0
    tmp = 0
    start = 0
    
    for i in range(1, len(A)):
        profit = A[i] - A[start]
        if profit > 0:
            tmp = profit
        else:
            start = i
        
        ans = max(tmp, ans)
    
    return ans

A = [23171, 21011, 21123, 21366, 21013, 21367]
A = [0, 0]
A = []
A = [1, 200000, 0, 200000]
print(solution(A))