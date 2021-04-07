class Solution:
    def titleToNumber(self, columnTitle):
        
        N = len(columnTitle) 
        power = (N - 1)
        ret = 0
        
        for i in range(N):
            digit = ord(columnTitle[i]) - 64
            ret += digit * (26 ** power)
            power -= 1
        
        return ret 

sol = Solution()
print(sol.titleToNumber("AA"))    # 27