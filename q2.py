# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ""
        s2 = ""
        
        while l1 != None:
            s1 += str(l1.val)
            l1 = l1.next
        
        while l2 != None:
            s2 += str(l2.val)
            l2 = l2.next
        
        _sum = list(str(int(s1[::-1]) + int(s2[::-1]))[::-1])
        l3 = ListNode(_sum[0])
        print(_sum)
        
        if len(_sum) < 2:
            return l3
        
        ptr = l3
        for i in range(1, len(_sum)):
            ptr.next = ListNode(_sum[i])
            ptr = ptr.next
        
        return l3
        