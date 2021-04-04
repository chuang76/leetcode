def solution(A):
    
    if len(A) == 3:
        return A[0] * A[1] * A[2]
    
    A.sort()
    
    if A[0] >= 0:
        return A[-3] * A[-2] * A[-1]
    
    if A[-1] < 0:
        return A[-3] * A[-2] * A[-1]       
    
    # 2 neg * 1 pos
    if A[0] * A[1] * A[-1] > A[-3] * A[-2] * A[-1]:
        return A[0] * A[1] * A[-1]
    
    return A[-3] * A[-2] * A[-1]

A = [4, 7, 3, 2, 1, -3, -5]
print(solution(A))                  # 105 