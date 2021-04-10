# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# inorder traversal first, then check if it is strictly increasing 
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        self.arr = []
        self.inorder(root)
        
        if len(self.arr) == 1:
            return True
        
        sorted(self.arr)
        # print(self.arr)
        
        for i in range(1, len(self.arr)):
            if self.arr[i] <= self.arr[i-1]:
                return False
        
        return True
    
    def inorder(self, root):
        
        if root == None:
            return
        
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)
        