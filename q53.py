# Maximum Subarray

class Solution:
    def maxSubArray(self, nums):
        if (max(nums) < 0):
            return max(nums)
        
        if (len(nums) == 1):
            return nums[0]
        
        start, end, ans, tmp = 0, 0, 0, 0  

        for i in range(0, len(nums)):

            if (tmp + nums[i]) < 0:                
                start, end = i + 1, i + 1        
                tmp = 0
            else:
                end = i + 1
                tmp += nums[i]
                if ans < tmp:
                    ans = tmp
            
        return ans