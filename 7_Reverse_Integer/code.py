class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        
        if x < 0:
            x *= -1
            while x > 0:
                tmp = x % 10
                x //= 10
                res = res * 10 + tmp
                if res > 2**31 - 1: return 0
            res *= -1
        else:
            while x > 0:
                tmp = x % 10
                x //= 10
                res = res * 10 + tmp
                if res > 2**31 - 1: return 0
                
        return res
            