class Solution:
    def isPalindrome(self, s):
        
        arr = []
        for i in range(len(s)):
            if s[i].isalnum():
                arr.append(s[i].lower())
                
        arr = "".join(arr)
        if arr == arr[::-1]:
            return True
        
        return False


s = "A man, a plan, a canal: Panama"      # true
s = "race a car"                          # false
s = "0P"                                  # false
sol = Solution()
print(sol.isPalindrome(s))