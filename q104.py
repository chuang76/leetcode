# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root):
        
        if root == None:
            return 0
        
        ldepth = self.maxDepth(root.left)
        rdepth = self.maxDepth(root.right)
        print('root = %d, ldeph = %d, rdepth = %d' %(root.val, ldepth, rdepth))
        
        if ldepth > rdepth:
            return ldepth + 1
        else:
            return rdepth + 1
            

# Input: [3, 9, 20, null, null, 15, 7]
# root = 9, ldeph = 0, rdepth = 0
# root = 15, ldeph = 0, rdepth = 0
# root = 7, ldeph = 0, rdepth = 0
# root = 20, ldeph = 1, rdepth = 1
# root = 3, ldeph = 1, rdepth = 2
        