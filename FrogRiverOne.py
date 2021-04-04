# Solution 1: too slow 
def solution(X, A):
    
    table = [False] * X        
    done = [True] * X
    
    for i in range(len(A)):
        table[A[i]-1] = True
        if table == done:
            return i
    
    return -1

# Solution 2: use an integer to record 
def solution(X, A):
    
    table = [False] * X        
    count = 0
    
    for i in range(len(A)):
        if table[A[i]-1] == False:
            table[A[i]-1] = True
            count += 1
        
        if count == X:
            return i
    
    return -1

A = [1, 3, 1, 4, 2, 3, 5, 4]
print(solution(5, A))           # 6 