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