def solution(S, T):
    
    if S == T:
        return "Equal"
    
    if S == T[:len(S)] and len(T) == len(S) + 1:
        return "Insert " + T[-1]

    if T == S[1:] and len(S) == len(T) + 1:
        return "Remove " + S[0]
    
    if len(S) != len(T):
        return "Impossible"
    
    swap = 0
    for i in range(len(S)):
        
        if S[i] == T[i]:
            continue
            
        for j in range(len(T)):
            if T[j] == S[i] and S[j] == T[i]:
                swap += 1
                x, y = S[i], T[i]
        if swap == 0:
            print('!')
            return "Impossible"
    
    if swap > 2:
        return "Impossible"
    
    return "Swap " + x + " " + y