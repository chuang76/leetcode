class Solution:
    def addToArrayForm(self, num, k):
        return list(str(int("".join(str(i) for i in num)) + k))