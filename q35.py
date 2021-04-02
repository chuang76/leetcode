class Solution:
    def searchInsert(self, nums, target) -> int:
        
        if nums[0] >= target:
            return 0
        
        if nums[-1] == target:
            return len(nums)-1
        
        if nums[-1] < target:
            return len(nums)
        
        for i in range(len(nums)-1):
            if nums[i] == target:
                return i
            if nums[i] < target and target < nums[i+1]:
                return (i+1)


# Solution 2: binary search (since the input array is sorted)

class Solution:
    def searchInsert(self, nums, target) -> int:
        if nums[0] >= target:
            return 0
        
        if nums[-1] < target:
            return len(nums)
        
        return self.search(nums, 0, len(nums)-1, target)    
    
    def search(self, nums, start, end, target):
        if start > end:
            return start
        mid = start + (end - start) // 2
        if nums[mid] > target:
            return self.search(nums, start, mid-1, target)
        if nums[mid] < target:
            return self.search(nums, mid+1, end, target)
        return mid