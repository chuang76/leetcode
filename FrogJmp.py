def solution(X, Y, D):
    ans = (Y - X) / D
    ans = int(-(-ans // 1))        # ceil
    return ans

print(solution(10, 85, 30))