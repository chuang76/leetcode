# Solution 1: TLE due to copy the stack 

def solution(S):
    
    if len(S) == 0:
        return 1
    
    if len(S) % 2 != 0:
        return 0
    
    if S[0] == ')' or S[0] == ']' or S[0] == '}':
        return 0
    
    stack = []
    
    for i in range(len(S)):
        
        if S[i] == ')':
            if len(stack) == 0:
                return 0
            elif stack[-1] != '(':
                return 0
            else:
                stack = stack[:-1]
        elif S[i] == ']':
            if len(stack) == 0:
                return 0
            elif stack[-1] != '[':
                return 0
            else:
                stack = stack[:-1]
        elif S[i] == '}':
            if len(stack) == 0:
                return 0
            elif stack[-1] != '{':
                return 0
            else:
                stack = stack[:-1]
        else:
            stack.append(S[i])
        
    if len(stack) == 0:
        return 1
    
    return 0

S = "{[()()]}"
S = "([)()]"
S = ")("
S = "())(()"
print(solution(S))

# Solution 2: use a variable to record where is the top 
def solution(S):
    
    if len(S) == 0:
        return 1
    
    if len(S) % 2 != 0:
        return 0
    
    if S[0] == ')' or S[0] == ']' or S[0] == '}':
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
                
        elif S[i] == ']':
            if top < 0:
                return 0
            elif stack[top] != '[':
                return 0
            else:
                top -= 1
                
        elif S[i] == '}':
            if top < 0:
                return 0
            elif stack[top] != '{':
                return 0
            else:
                top -= 1
                
        else:
            stack[top+1] = S[i]
            top += 1
            
    if top == -1:
        return 1
    
    return 0

S = "()[]"
S = "({{({}[]{})}}[]{})"
print(solution(S))