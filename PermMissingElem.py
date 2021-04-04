def solution(A):
    N = len(A) + 1
    total = (N * (N + 1)) // 2
    ans = total - sum(A)
    return ans

A = [2, 3, 1, 5]
print(solution(A))