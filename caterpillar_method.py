def method(A, s):
    
    
    N = len(A)
    start, end = 0, 0
    total = 0
    
    for end in range(N):
        
        while (start < N and total + A[start] <= s):
            total += A[start]
            start += 1
        
        if total == s:
            return True 
    
        # 扣掉當前, 從 start 開始
        total -= A[end]
    
    return False

A = [6, 2, 7, 4, 1, 3, 6]
s = 12
print(len(A))
print(method(A, s))           # True 