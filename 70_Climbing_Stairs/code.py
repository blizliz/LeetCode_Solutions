class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = []
        
        for i in range(n):
            if i == 0: steps.append(1)
            elif i == 1: steps.append(2)
            else: steps.append(steps[i - 1] + steps[i - 2])
        
        return steps[n - 1]
        