class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = (1 + len(nums)) / 2 * len(nums)
        
        for num in nums:
            sum -= num
            
        return int(sum)