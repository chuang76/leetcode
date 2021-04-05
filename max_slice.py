def max_slice(A):
    
    ans, tmp = 0, 0
    
    for i in range(len(A)):
        
        tmp = max(0, tmp + A[i])       # 加下一個, 看有沒有變負, 如果負就歸零
        ans = max(tmp, ans)            # update 
    
    return ans

A = [5, -7, 3, 5, -2, 4, -1]
print(max_slice(A))