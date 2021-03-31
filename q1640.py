class Solution:
    def canFormArray(self, arr, pieces):
        table = {}
        for ele, i in enumerate(arr):
            table[i] = ele
        try:
            # a is a list, a[0] = 1st element of a, mapping to the index 
            pieces.sort(key=lambda a : table[a[0]])
        except:
            return False 
        
        # sorted pieces 
        concat = []
        for ele in pieces:
            concat += ele
        
        if (concat == arr):
            return True
        return False

arr = [91, 4, 64, 78]
pieces = [[78], [4,64], [91]]
s = Solution()
print(s.canFormArray(arr, pieces))