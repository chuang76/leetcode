class Solution:
    def isAnagram(self, s, t):
        
        s, t = list(s), list(t)
        
        if len(s) != len(t):
            return False
        
        s.sort()
        t.sort()

        N = len(s)
        for i in range(N):
            if s[i] != t[i]:
                return False
        
        return True

sol = Solution()
print(sol.isAnagram("rat", "car"))     # False 