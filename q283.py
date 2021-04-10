class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nz = -1
        
        if len(nums) > 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    nz += 1
                    nums[nz] = nums[i]
        
            for i in range(nz+1, len(nums)):
                nums[i] = 0
        
        # print(nums)

nums = [0, 1, 0, 3, 12, 4]
nums = [1]
nums = [0, 1]
sol = Solution()
sol.moveZeroes(nums)