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

# Solution 2: use the first element to reorganize 
class Solution:
    def canFormArray(self, arr, pieces):
        mapping = {}
        for piece in pieces:
            mapping[piece[0]] = piece
        print('mapping =', mapping)             # mapping = {78: [78], 4: [4, 64], 91: [91]}
        
        ans = []
        for i in arr:
            if i in mapping:
                ans += mapping[i]
        
        return ans == arr