class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        map = {}
        
        for inx, num in enumerate(nums):
            comp = target - num
            if comp in map:
                return [inx, map[comp]]
            map[num] = inx
        