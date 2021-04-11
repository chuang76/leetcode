# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.arr = []
        self.postorder(root)
        return self.arr
    
    def postorder(self, root):
        
        if root == None:
            return 
        
        self.postorder(root.left)
        self.postorder(root.right)
        self.arr.append(root.val)