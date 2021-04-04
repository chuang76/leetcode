def solution(A, K):
    
    if len(A) < 1:
        return A
    
    for k in range(K):
        prev = A[0]
    
        for i in range(len(A)):

            if i == (len(A) - 1):
                A[0] = prev                       
            else:
                tmp = A[i+1]                      
                A[i+1] = prev                     
                prev = tmp    
    return A

A = []
print(solution(A, 4))

# Solution 2
def solution(A, K):
    
    if len(A) < 1:
        return A
    
    for i in range(K):
        A.insert(0, A[-1])
        A = A[:-1]

    return A

# Solution 3 
def solution(A, K):
    
    N = len(A)
    if N < 1:
        return A
    
    K = K % N
    A = A[-K:] + A
    A = A[:N]

    return A