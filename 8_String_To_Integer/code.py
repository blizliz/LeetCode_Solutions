class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        if not str: return 0
        
        match = re.match('[\s]*([+-]*\d+)', str)
        if not match: return 0
        
        num = 0
        s = match.group(1)
        
        sign = True if s[0] == '-' or s[0] == '+' else False
        
        if sign and s[1:].isdigit() or not sign and s.isdigit():
            if int(s) < -2**31:
                num = -2**31
            elif int(s) > 2**31 - 1:
                num = 2**31 - 1
            else:
                num = int(s)
        
        return num
            