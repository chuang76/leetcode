def search(A, x):
    N = len(A)
    start, end = 0, N-1
    ans = -1
    
    while (start <= end):
        mid = (start + end) // 2
        if A[mid] <= x:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    
    return ans


A = [3, 4, 2, 5, 7, 6]    
print(search(A, 5))             # 3