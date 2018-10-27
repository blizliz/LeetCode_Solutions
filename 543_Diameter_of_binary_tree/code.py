# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    res = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
            
        self.subDiameter(root)

        return self.res

    def subDiameter(self, root):
        if not root: return
        l = self.maxHeight(root.left)
        r = self.maxHeight(root.right)
        self.res = max(self.res, l + r)
        self.subDiameter(root.left)
        self.subDiameter(root.right)
        
    def maxHeight(self, root):
        if not root: return 0
        
        l = self.maxHeight(root.left)
        r = self.maxHeight(root.right)
        
        return max(l, r) + 1