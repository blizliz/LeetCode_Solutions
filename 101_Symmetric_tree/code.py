# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.check(root.left , root.right)
        
    def check(self, left, right):
        if not left and not right:
            return True
        if left and right:
            if left.val != right.val: return False
            elif not self.check(left.left, right.right) : return False
            elif not self.check(left.right, right.left) : return False
            else: return True
        else: return False