def solution(A, K, L):
    
    if len(A) < (K + L):
        return -1
    
    if len(A) == (K + L):
        return sum(A)
    
    K_start = 0
    K_end = K_start + K 
    
    L_start = K_end
    L_end = L_start + L
    
    arr = []
    
    # 移動 K sequence
    for K_start in range(len(A)):
        K_end = K_start + K
        if K_end >= len(A):
            break 
        
        for L_start in range(K_end, len(A)):
            L_end = L_start + L
            if L_end > len(A):
                break 
            print('K_start = %d, K_end = %d, L_start = %d, L_end = %d' %(K_start, K_end, L_start, L_end))
            arr.append(sum(A[K_start:K_end]) + sum(A[L_start:L_end]))
            
    
    L_start = 0
    L_end = L_start + L 
    
    K_start = L_end
    K_end = K_start + K
    
    # 換 L 先來
    for L_start in range(len(A)):
        L_end = L_start + L
        if L_end >= len(A):
            break 
        
        for K_start in range(L_end, len(A)):
            K_end = K_start + K
            if K_end > len(A):
                break 
            print('K_start = %d, K_end = %d, L_start = %d, L_end = %d' %(K_start, K_end, L_start, L_end))
            arr.append(sum(A[K_start:K_end]) + sum(A[L_start:L_end]))
        
    return max(arr)

A = [1, 100, 2, -1000, 200, 3]
K = 2
L = 3
print(solution(A, K, L))        # 306