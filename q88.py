class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = []
        lptr, rptr = 0, 0
        while lptr < m and rptr < n:
            if nums1[lptr] <= nums2[rptr]:
                tmp.append(nums1[lptr])
                lptr += 1
            else:
                tmp.append(nums2[rptr])
                rptr += 1
                
        tmp += nums1[lptr:m]
        tmp += nums2[rptr:n]
        nums1[:] = tmp
        