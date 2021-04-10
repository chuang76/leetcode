class Solution:
    def sortedSquares(self, nums):
        arr = sorted(nums, key=lambda x: (x ** 2, x))
        return [(x ** 2) for x in arr]

nums = [-4, -1, 0, 3, 10]
sol = Solution()
print(sol.sortedSquares(nums))    # [0, 1, 9, 16, 100]

# Solution 2: sqrt first then sort 
class Solution:
    def sortedSquares(self, nums):
        arr = [(x ** 2) for x in nums]
        arr.sort()
        return arr