class Solution: 
    def maxProfit(self, prices):
        
        arr = []
        N = len(prices)
        
        for i in range(1, N):
            profit = prices[i] - prices[i-1]
            if profit > 0:
                arr.append(profit)
        
        return sum(arr)

sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))    # 7