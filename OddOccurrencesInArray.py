def solution(A):
    
    if len(A) < 1:
        return None
    
    unique = 0
    for i in A:
        unique ^= i
    return unique

A = [9, 3, 9, 3, 9, 7, 9]
print(solution(A))