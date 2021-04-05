def solution(S):
    
    # empty
    if len(S) == 0:
        return 1
    
    # odd
    if len(S) % 2 != 0:
        return 0
    
    if S[0] == ')':
        return 0
    
    stack = ['_'] * len(S)
    top = -1
    
    for i in range(len(S)):
        if S[i] == ')':
            if top < 0:
                return 0
            elif stack[top] != '(':
                return 0
            else:
                top -= 1
        else:
            top += 1
            stack[top] = S[i]
    
    if top == -1:
        return 1
    
    return 0

S = "(()(())())"
S = "())"
S = "()((()))"
S = ""
print(solution(S))