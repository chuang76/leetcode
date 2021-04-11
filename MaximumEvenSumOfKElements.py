def ans(A, K):
    
    N = len(A)
    
    # 排不出來
    if N < K:
        return -1

    # 只有 K 個
    if N == K:
        tmp = sum(A)
        if tmp % 2 != 0:
            return -1 
        else:
            return tmp
    
    A.sort()
    
    even, odd = [], []
    for i in range(len(A)):
        if A[i] % 2 == 0:
            even.append(A[i])
        else:
            odd.append(A[i])
    
    # 可以有的個數
    odd_num = [(x * 2) for x in range(len(odd)//2 + 1)]
    even_num = [x for x in range(len(even) + 1)]
    
    ans = -1
    # 奇數 + 偶數
    for i in odd_num:
        
        if i == 0:
            continue 
        
        # i 個奇數 + j 個偶數
        j = K - i
        
        if j not in even_num:
            continue
            
        if j == 0:
            tmp = sum(odd[-i:])
        else:
            tmp = sum(odd[-i:]) + sum(even[-j:])
        
        if tmp % 2 == 0:
            ans = max(ans, tmp)
        
    # 全部偶數
    ans = max(ans, sum(even[-K:]))
    return ans