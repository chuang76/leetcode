# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root):
        return self.check(root.left, root.right)
    
    def check(self, lptr, rptr):
        
        if lptr == None and rptr == None:
            return True
    
        if lptr == None or rptr == None:
            return False
        
        return (lptr.val == rptr.val) and self.check(lptr.left, rptr.right) and self.check(lptr.right, rptr.left)
        