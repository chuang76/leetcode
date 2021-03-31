class Solution:
    def restoreString(self, s, indices):
        arr = list(s)     # an array of characters
        table = {}
        for i in range(len(arr)):
            table[indices[i]] = arr[i]

        sorted_table = sorted(table.items())
        ans = ""
        for k, v in sorted_table:
            ans += v
        return ans 

sol = Solution()
s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]      # leetcode 
print(sol.restoreString(s, indices))