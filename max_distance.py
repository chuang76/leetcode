def solution(x, y):
    arr = []
    
    for i in range(len(x)):
        
        rem_x = x[:i] + x[i+1:]
        rem_y = y[:i] + y[i+1:]
        
        local_arr = []
        for j in range(len(rem_x)):
            local_arr.append(pow(abs(rem_x[j] - x[i]), 2) + pow(abs(rem_y[j] - y[i]), 2))
            
        arr.append(max(local_arr))
    
    return max(arr)