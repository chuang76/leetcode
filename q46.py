class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return []
    
        if len(nums) == 1:
            return [nums]
        
        arr = []
        for i in range(len(nums)):
            k = [nums[i]]
            rem = nums[:i] + nums[i+1:]
            
            for j in self.permute(rem):
                arr.append(k + j)
        
        return arr
                
            