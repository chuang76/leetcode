class Solution:
    def reverseList(self, head):
        
        if head == None:
            return head 
        
        ptr = head
        next_ptr = None          # 多記一個 next
        tail = None
                  
        while (ptr != None):
            next_ptr = ptr.next       # 記起來
            ptr.next = tail           # 改指到 tail 
            tail = ptr 
            ptr = next_ptr 
        
        return tail