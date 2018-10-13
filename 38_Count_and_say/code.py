class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        if n == 1: return s
        for i in range(n-1):
            s = self.step(s)
        return s
    
    def step(self, n):
        if len(n) == 1: return "11"
        res = ""
        prev = n[0]
        count = 1
        for ch in n[1:]:
            if ch == prev:
                count += 1
            else:
                res = res + str(count) + str(prev)
                prev = ch
                count = 1
        res = res + str(count) + str(prev)
        return res