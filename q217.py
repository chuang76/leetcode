class Solution:
    def containsDuplicate(self, nums):
        if len(nums) == 1:
            return False
        
        table = {}
        N = len(nums)
        for i in range(N):
            val = nums[i]
            if val in table:
                return True
            else:
                table[val] = val
            
        return False

sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 1]) )  # True
