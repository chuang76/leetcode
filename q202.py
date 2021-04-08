class Solution:
    def isHappy(self, n):
        print(n)
        
        if n == 1:
            return True
        
        visited = {}
        
        while n != 1:
            _sum = sum([int(i) ** 2 for i in str(n)])
            if _sum not in visited:
                visited[_sum] = _sum
                n = _sum
            else:
                return False
        
        return True


# Solution 2: check table
class Solution:
    def isHappy(self, n):
        
        table = [True, False, False, False, False, False, True, False, False]
        
        if n < 10:
            return table[n-1]
        
        sqrt = {'0': 0, '1': 1, '2': 4, '3': 9, '4': 16, '5': 25, \
                '6': 36, '7': 49, '8': 64, '9': 81}
        
        n = str(n)
        while len(n) > 1:
            _sum = 0
            for i in range(len(n)):
                _sum += sqrt[n[i]]   
            if _sum < 10:
                return table[_sum-1]
            n = str(_sum)

sol = Solution()
print(sol.isHappy(11))     # False 