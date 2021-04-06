class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        if x < 10:
            return True
        
        reverse = int(str(x)[::-1])

        if reverse == x:
            return True
        
        return False

sol = Solution()
print(sol.isPalindrome(121))
