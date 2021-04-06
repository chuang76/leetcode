def solution(A):
    
    for i in range(len(A)):
        
        if A[i] >= 0:
            break 
        
        A[i] = abs(A[i])
    
    return len(set(A))

A = [-5, -3, -1, 0, 3, 6]
A = [0, 0, 0]
A = []
A = [-1, -9, -2, -2147483647]
A = [2147483647, 2147483647, 2147483647, 2147483647]
print(solution(A))