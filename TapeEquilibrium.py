# each element of array A is an integer within the range [−1,000..1,000]

def solution(A):
    
    total = sum(A)
    a = 0
    ans = 2001
    
    for i in range(len(A)-1):
        a += A[i]
        b = total - a
        diff = abs(total - 2 * a)
        if diff < ans:
            ans = diff
    
    return ans

A = [3, 1, 2, 4, 3]
print(solution(A))