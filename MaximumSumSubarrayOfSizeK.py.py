'''
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''

def solution(A, K):
    ans = 0
    for i in range(len(A)-K+1):
        ans = max(sum(A[i:i+K]), ans)
    
    return ans

# Solution 2
def solution(A, K):
    
    max_sum, local_sum = 0, 0
    start = 0
    
    for end in range(len(A)):
        local_sum += A[end]
        
        while end >= K-1:
            max_sum = max(max_sum, local_sum)
            local_sum -= A[start]              # 滑出
            start += 1
    
    return max_sum