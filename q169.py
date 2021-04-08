class Solution:
    def majorityElement(self, nums):
        
        N = len(nums)
        
        if N == 1:
            return nums[0]
        
        nums.sort()
        candidate = nums[N // 2]
        return candidate

nums = [3, 2, 3]
sol = Solution()
print(sol.majorityElement(nums))     # 3