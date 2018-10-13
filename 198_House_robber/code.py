class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        
        rob = [nums[0], nums[1], nums[0] + nums[2]]
        
        for i in range(3, len(nums)):
            rob.append(max(nums[i] + rob[i - 2], nums[i] + rob[i - 3]))
            
        return max(rob[len(rob) - 1], rob[len(rob) - 2])