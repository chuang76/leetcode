def solution(N):
    
    if (N < 5):
        return 0
    
    arr = "{0:b}".format(N)         # binary representation 
    
    ans, tmp = 0, 0
    flag = 0
    
    for i in range(len(arr)):
        
        if flag == 0:
            if arr[i] == '0':
                continue
            if arr[i] == '1':
                tmp = 0 
                flag = 1
        else:
            if arr[i] == '1':
                if ans < tmp:
                    ans = tmp
                tmp = 0
            else:
                tmp += 1
        
    if flag == 0:
        return 0

    return ans

print(solution(1041))