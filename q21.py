# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        
        tmp1 = l1
        tmp2 = l2
        flag = 0
        head = None
        
        if (tmp1 == None and tmp2 == None):
            return None
        
        if (tmp1 == None):
            while (tmp2 != None):
                if head == None:
                    head = ListNode(tmp2.val)
                    ptr = head
                else:
                    ptr.next = ListNode(tmp2.val)
                    ptr = ptr.next 
                tmp2 = tmp2.next
            return head
        
        if (tmp2 == None):
            while (tmp1 != None):
                if head == None:
                    head = ListNode(tmp1.val)
                    ptr = head
                else:
                    ptr.next = ListNode(tmp1.val)
                    ptr = ptr.next 
                tmp1 = tmp1.next
        
        while (tmp1 != None and tmp2 != None):
            # head 
            if head == None:
                if tmp1.val < tmp2.val:
                    node = ListNode(tmp1.val)          # 創 head, l1 先放
                    head = node
                    tmp1 = tmp1.next
                else:
                    node = ListNode(tmp2.val)
                    head = node
                    tmp2 = tmp2.next
                ptr = head                             # 放完之後, 用一個指標指向 head
            else:
                if tmp1.val < tmp2.val:
                    node = ListNode(tmp1.val)  
                    ptr.next = node 
                    ptr = node                         # 指向 node
                    tmp1 = tmp1.next
                else:
                    node = ListNode(tmp2.val)  
                    ptr.next = node 
                    ptr = node                         # 指向 node
                    tmp2 = tmp2.next
                    
        while (tmp1 != None):
            node = ListNode(tmp1.val)
            ptr.next = node
            ptr = node
            tmp1 = tmp1.next
        
        while (tmp2 != None):
            node = ListNode(tmp2.val)
            ptr.next = node
            ptr = node
            tmp2 = tmp2.next
        
        return head

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(4)
a1.next = a2
a2.next = a3

b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)
b1.next = b2
b2.next = b3

c1 = ListNode(5)

sol = Solution()
ret = sol.mergeTwoLists(a1, b1)             
tmp = ret
while tmp != None:
    print(tmp.val)               # 1, 1, 2, 3, 4, 4 
    tmp = tmp.next


# Solution 2: use pointer to operate 
class Solution:
    def mergeTwoLists(self, l1, l2):
        
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        
        ptr = head
        while (l1 and l2):
            if l1.val <= l2.val:
                ptr.next = l1
                ptr = ptr.next
                l1 = l1.next
            else:
                ptr.next = l2
                ptr = ptr.next
                l2 = l2.next
        
        if not l1:
            ptr.next = l2
        else:
            ptr.next = l1
        
        return head