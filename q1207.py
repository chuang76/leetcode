class Solution:
    def uniqueOccurrences(self, arr):
        table = []
        for i in range(2001):
            table.append(0)                      
        for i in arr:
            table[i+1000] = table[i+1000] + 1    
            
        if (sum(set(table)) == sum(table)):
            return True
        return False

s = Solution()
arr = [1, 2, 2, 1, 1, 3]
print(s.uniqueOccurrences(arr))