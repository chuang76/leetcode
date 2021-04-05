def solution(A, B):
    
    stack = ['_'] * len(A)
    flag = 0
    live = 0
    top = -1 
    
    for i in range(len(A)):
        
        print('A[%d] = %d, live = %d, top = %d' %(i, A[i], live, top))
        print('stack =', stack)
        print('---------------------------------------')
        
        if B[i] == 0 and flag == 0:
            live += 1
        
        # down
        elif B[i] == 1:
            flag = 1
            top += 1
            stack[top] = A[i]
        
        # up
        elif B[i] == 0 and flag == 1:
            
            # empty stack
            if top < 0:
                live += 1
                continue
            
            up = 1              
            while top >= 0:
                if A[i] > stack[top]:
                    top -= 1
                else:
                    up = 0
                    break 
            
            # win
            if up == 1:
                live += 1
    
    return live + (top + 1)

A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]
print(solution(A, B))