class Solution:
    def reverse(self, x):
        
        if x > -10 and x < 10:
            return x
        
        sign = 0
        if x < 0:
            sign = 1         # negative 
            x = -x
        
        top = -1
        stack = []
        while x:
            stack.append(x % 10)
            top += 1
            x = x // 10
        
        # pop
        ans = 0
        num = 0 
        while top >= 0:
            tmp = stack[top] * (10 ** num)
            ans += tmp
            num += 1
            top -= 1
        
        if sign:
            ans = -ans
            if ans > (2 ** 31 - 1) or ans < (-2 ** 31):
                return 0
            else:
                return ans
        else:
            if ans > (2 ** 31 - 1) or ans < (-2 ** 31):
                return 0
            else:
                return ans

# Solution: string to integer
class Solution:
    
    def reverse(self, x):
        
        # reverse
        ret = int(str(abs(x))[::-1])
        
        if ret.bit_length() > 31:
            return 0
        
        if x < 0:
            return -ret
        
        return ret

sol = Solution()
print(sol.reverse(1534236469))       # 0
print(sol.reverse(123))
print(sol.reverse(-123))
print(sol.reverse(120))              # 21 