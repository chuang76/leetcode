class Solution:
    def romanToInt(self, s):
        
        N = len(s)
        table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        if N == 1:
            return table[s[0]]
        
        ans = 0
        ans += table[s[0]]
        for i in range(1, len(s)):
            if table[s[i]] > table[s[i-1]]:
                ans += table[s[i]] - (table[s[i-1]] * 2)
            else:
                ans += table[s[i]]

        return ans

sol = Solution()
print(sol.romanToInt("IX"))        # 9
print(sol.romanToInt("LVIII"))     # 58 
print(sol.romanToInt("MCMXCIV"))   # 1994