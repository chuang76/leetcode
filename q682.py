class Solution:
    def calPoints(self, ops):
        
        stack = ["_"] * len(ops)
        
        top = -1
        for i in range(len(ops)):
            
            if ops[i] == "C":
                top -= 1          # pop
            
            elif ops[i] == "D":
                stack[top + 1] = stack[top] * 2n
                top += 1
            
            elif ops[i] == "+":
                stack[top + 1] = stack[top] + stack[top-1]
                top += 1
            
            else:
                stack[top + 1] = int(ops[i])
                top += 1
        
        _sum = sum([stack[i] for i in range(0, top+1)])
        return _sum

ops = ["5", "2", "C", "D", "+"]                     # 30
ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]     # 27
ops = ["1"]                                         # 1
sol = Solution()
print(sol.calPoints(ops))