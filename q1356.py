class Solution:
    def sortByBits(self, arr):
        
        if len(arr) == 1:
            return arr
        
        return sorted(arr, key=lambda x: (bin(x).count("1"), x))


arr = [10000, 10000, 1]
arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
sol = Solution()
print(sol.sortByBits(arr))