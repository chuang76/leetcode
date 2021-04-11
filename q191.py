class Solution:
    def hammingWeight(self, n):
        binary = "{0:032b}".format(n)
        count = 0
        for i in binary:
            if i == '1':
                count += 1
        
        return count

sol = Solution()
print(sol.hammingWeight(4294967293))    # 31

# use count function 
class Solution:
    def hammingWeight(self, n):
        binary = "{0:032b}".format(n)
        return binary.count("1")