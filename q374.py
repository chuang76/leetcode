# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n):
        
        if n == 1:
            return 1
    
        lptr, rptr = 1, n
        
        while lptr < rptr:
            mid = (lptr + rptr) // 2
            ret = guess(mid)
            
            if ret == -1:
                rptr = mid - 1
            elif ret == 0:
                return mid 
            else:
                lptr = mid + 1
        
        return lptr