# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if not nums: return None
        mid = len(nums) // 2
        res = TreeNode(nums[mid])
        res.left = self.sortedArrayToBST(nums[0 : mid])
        res.right = self.sortedArrayToBST(nums[mid + 1 : len(nums)])
        
        return res