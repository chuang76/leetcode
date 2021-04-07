class Solution:
    def reverseBits(self, n):
        binary = "{0:032b}".format(n)      # 32-bit 
        rev = binary[::-1]                 # reverse
        return int(rev, 2)                 # string to integer 