class Solution:
    def removeDuplicates(self, nums):
        
        # return length 
        if (len(nums) == 0):
            return 0
        
        N = len(nums)
        unique = 0
        
        for i in range(1, N):
            if nums[i] != nums[unique]:        
                unique += 1                     # 有不一樣的, copy 進來
                nums[unique] = nums[i]             
        
        # print('nums =', nums)
        
        return unique + 1

sol = Solution()
nums = [1, 2, 2, 3]
print(sol.removeDuplicates(nums))