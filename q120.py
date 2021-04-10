# use prefix sum 

class Solution:
    def minimumTotal(self, triangle):
        
        if len(triangle) == 1:
            return triangle[0][0]  
        
        for i in range(1, len(triangle)):
            
            for j in range(0, len(triangle[i])):
                
                if j == 0:
                    triangle[i][j] += triangle[i-1][0]
                elif j == len(triangle[i])-1:
                    triangle[i][j] += triangle[i-1][-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        
        return min(triangle[-1])