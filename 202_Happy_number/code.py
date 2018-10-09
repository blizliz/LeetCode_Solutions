class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        
        while n != 1:
            s.add(n)
            n = self.getSum(n)
            if n in s: return False
            
        return True
        
    def getSum(self, num):
        res = 0
        while num != 0:
            res += (num % 10) * (num % 10)
            num //= 10
        return res