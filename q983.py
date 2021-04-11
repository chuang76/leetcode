class Solution:
    def mincostTickets(self, days, costs):
        table = [0] * (days[-1] + 1)
        
        for i in range(1, len(table)):
            
            # 有買票
            if i in days:
                # 直接買一天
                if i >= 30:
                    table[i] = min(table[i-1] + costs[0], table[i-7] + costs[1], table[i-30] + costs[2])
                elif i >= 7:
                    table[i] = min(table[i-1] + costs[0], table[i-7] + costs[1], costs[2])
                else:
                    table[i] = min(table[i-1] + costs[0], costs[1], costs[2])
            else:
                table[i] = table[i-1]
            
        return table[-1]