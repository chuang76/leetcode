class Solution:
    def countNegatives(self, grid):
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    ans = ans + (len(grid[i]) - j)
                    break
        return ans

grid = [[4,3,2,-1], [3,2,1,-1], [1,1,-1,-2], [-1,-1,-2,-3]]
s = Solution()
print(s.countNegatives(grid))

# Solution 2: use sum()
class Solution:
    def countNegatives(self, grid):
        # count 
        return len([i for i in sum(grid,[]) if i < 0])

# solution 3
class Solution:
    def countNegatives(self, grid):

        ans = 0
        j = len(grid[0]) - 1
        
        for i in range(len(grid)):      

            while j >= 0:
                if grid[i][j] >= 0:
                    break 
                else:
                    j -= 1
            
            ans += len(grid[0])-1-j
                    
        return ans