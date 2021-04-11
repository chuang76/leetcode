class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        
        ans, total = 0, 0
        
        for i in range(len(boxTypes)):
            
            if total >= truckSize:
                break
            
            tmp = boxTypes[i][0]
            
            if (total + tmp) > truckSize:
                tmp = truckSize - total 
                
            total += tmp
            ans += (tmp * boxTypes[i][1])
        
        return ans

boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
truckSize = 10
sol = Solution()
print(sol.maximumUnits(boxTypes, truckSize))   # 91