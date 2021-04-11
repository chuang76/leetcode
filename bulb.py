def solution(A):
    
    check = [0] * (max(A))
    
    ans = 0
    for i in range(len(A)):
        
        if check[A[i]-1] == 0:
            check[A[i]-1] = 1        # 改成 1
        
        if sum(check[:A[i]]) == A[i]:
            ans += 1
        
    return ans