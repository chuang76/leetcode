def solution(N, A):
    table = [0] * N
    max_value = 0
    
    for i in range(len(A)):
        
        x = (A[i] - 1)                      
        
        if A[i] == (N+1):
            table = [max_value] * N
        else:
            table[x] += 1
            if table[x] > max_value:
                max_value = table[x]
    
    return table


A = [2, 1, 1, 2, 1]
N = 1
print(solution(N, A))       # 3