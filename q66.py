class Solution:
    def plusOne(self, digits):
        a = int("".join(str(i) for i in digits)) + 1
        a = list(str(a))
        return a