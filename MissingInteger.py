def solution(A):
    
    table = [False] * 1000000
    
    for i in range(len(A)):
        
        if A[i] < 0:
            continue 
        
        table[A[i]-1] = True      
    
    for i in range(len(table)):
        if table[i] == False:
            return (i+1)

A = [-1000000, 1000000]
print(solution(A))              # 1


# Solution 2: sort first
def solution(A):

    if max(A) < 0:
        return 1 
    
    # return 1 directly 
    if 1 not in A:
        return 1
    
    B = [x for x in A if x > 0]
    B.sort()
    
    # 1, 3, 4, ... 
    for i in range(len(B)-1):
        if B[i+1] - B[i] > 1:
            return B[i] + 1
    
    return max(B) + 1