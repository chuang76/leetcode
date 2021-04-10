class Solution:
    def addBinary(self, a, b):
        return "{0:b}".format(int(a, 2) + int(b, 2))

sol = Solution()
a = "11"
b = "1"
print(sol.addBinary(a, b))     # 100