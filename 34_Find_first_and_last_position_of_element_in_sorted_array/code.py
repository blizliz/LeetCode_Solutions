class Solution:
    def leftBinSearch(self, nums, key):
        l = -1
        r = len(nums)
        while l < r - 1:
            m = (l + r) // 2
            if key > nums[m]:
                l = m
            else:
                r = m
        if r != len(nums) and nums[r] == key: return r
        else: return -1
        
    def rightBinSearch(self, nums, key):
        l = -1
        r = len(nums)
        while l < r - 1:
            m = (l + r) // 2
            if key >= nums[m]:
                l = m
            else:
                r = m
        if l != len(nums) and nums[l] == key: return l
        else: return -1
        
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1, -1]
        l = self.leftBinSearch(nums, target)
        r = self.rightBinSearch(nums, target)
        return [l, r]
            