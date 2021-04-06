def solution(M, A):
    
    if len(A) == 1:
        return 1
    
    used = [0] * (M + 1)       # [0, 1, 2, ..., M]
    N = len(A)
    lptr, rptr = 0, 0
    ans = 0
    
    while rptr < N:
        
        if used[A[rptr]] == 0:
            used[A[rptr]] = 1
            rptr += 1
    
        else:
            tmp = lptr
            # clear
            while used[A[rptr]] != 0:
                used[A[lptr]] = 0
                lptr += 1
                
            a = (rptr - 1 - tmp + 1)     
            b = rptr - lptr 
            a = (a * (a + 1)) // 2
            b = (b * (b + 1)) // 2
            ans += (a - b)
            
    
    # border
    rptr -= 1
    n = rptr - lptr + 1
    ans += (n * (n + 1)) // 2
    
    return min(ans, 1000000000)