class Solution:
    def findShortestSubArray(self, nums):
        C = {}
        for i, n in enumerate(nums):
            if n in C:
                C[n].append(i)                       # postion (idx)
            else:
                C[n] = [i]
        
        M = max([len(i) for i in C.values()])        # max freq 
        
        ans = len(nums)
        for i in C.values():
            if len(i) == M:
                tmp = i[-1] - i[0]
                if tmp < ans:
                    ans = tmp
        
        return ans + 1

nums = [1, 2, 2, 3, 1]
sol = Solution()
print(sol.findShortestSubArray(nums))                 # 2
# C = {1: [0, 4], 2: [1, 2], 3: [3]}