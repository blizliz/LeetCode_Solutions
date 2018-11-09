# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        else:
            root.left = self.invertTree(root.left)
            root.right = self.invertTree(root.right)
            tmp = root.right
            root.right = root.left
            root.left = tmp
            return root