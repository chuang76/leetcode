def solution(s):
    
    if len(s) == 1:
        return -1 

    for i in range(len(s)):
        left = s[:i+1].count("(")
        right = s[i+1:].count(")")
        if left == right:
            return i
    
    return -1