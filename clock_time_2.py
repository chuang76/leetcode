def solution(A):
    
    A = sorted(A, reverse=True)
    h, m, s = -1, -1, -1
    
    for i in range(len(A)):
        if A[i] > 23:
            continue 
        h = i
        break 
    
    if h == -1:
        return -1
    
    for i in range(len(A)):
        if i == h:
            continue
        if A[i] > 59:
            continue
        m = i
        break 
    
    if m == -1:
        return -1
    
    for i in range(len(A)):
        if i == h or i == m:
            continue
        if A[i] > 59:
            continue
        s = i
        break
    
    if s == -1:
        return -1 
    
    if A[h] < 0 or A[m] < 0 or A[s] < 0:
        return -1 
    
    return "{:0>2d}:{:0>2d}:{:0>2d}".format(A[h], A[m], A[s])