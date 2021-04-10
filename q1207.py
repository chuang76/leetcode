class Solution:
    def uniqueOccurrences(self, arr):

        table = [0] * 2001
        for i in arr:
            table[i+1000] = table[i+1000] + 1    
            
        if (sum(set(table)) == sum(table)):
            return True
        return False

s = Solution()
arr = [1, 2, 2, 1, 1, 3]
print(s.uniqueOccurrences(arr))

# Solution 2: use sort
class Solution:
    def uniqueOccurrences(self, arr):
        table = [0] * 2001
        for i in arr:
            table[i+1000] = table[i+1000] + 1    
            
        new_table = [i for i in table if i != 0]
        new_table.sort()
        
        for i in range(1, len(new_table)):
            if new_table[i] == new_table[i-1]:
                return False
        
        return True