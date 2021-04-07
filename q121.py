class Solution:
    def maxProfit(self, prices):
        
        if len(prices) < 2:
            return 0
        
        ret = 0
        tmp = 0
        start = 0
        
        for i in range(1, len(prices)):
            
            profit = prices[i] - prices[start]
            
            if profit > 0:
                tmp = profit       
            else:
                start = i
                
            ret = max(ret, tmp)
        
        return ret

sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))    # 5 