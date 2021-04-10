# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        lptr, rptr = 1, n
        while (lptr < rptr):
            mid = (lptr + rptr) // 2
            if isBadVersion(mid) == True:       
                rptr = mid
            else:                                 
                lptr = mid + 1
        
        # first True
        return lptr