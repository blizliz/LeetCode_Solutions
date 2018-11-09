class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.binSearch(nums, 0, len(nums) - 1)
        
    def binSearch(self, nums, l ,r):
        if l == r:
            return l
        m = (l + r) // 2
        if nums[m] > nums[m + 1]:
            return self.binSearch(nums, l, m)
        return self.binSearch(nums, m + 1, r)
        
        