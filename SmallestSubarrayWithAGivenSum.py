'''
Problem Statement 
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.
Example 1:
Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
Example 2:
Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:
Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
'''

# 最短的 subarray 可以 >= K 
def solution(A, K):
    
    if sum(A) < K:
        return 0
    
    min_len = len(A)
    for i in range(0, len(A)-1):
        tmp = A[i]
        local_len = 1
        
        if tmp >= K:
            return 1
        
        for j in range(i+1, len(A)):
            tmp += A[j]
            if tmp >= K:
                local_len = j - i + 1
                min_len = min(min_len, local_len)
                break 
    
    return min_len

# Solution 2: use sliding window 
def solution(A, K):
    
    local_sum = 0
    length = len(A) + 1
    start = 0
    
    for end in range(len(A)):
        local_sum += A[end]
        
        while local_sum >= K:
            # 太大了, 退掉 start 
            length = min(length, end-start+1)
            local_sum -= A[start]
            start += 1
        
    if length == len(A) + 1:
        return 0
    
    return length