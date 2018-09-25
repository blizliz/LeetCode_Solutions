class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = ""
        
        if numRows == 1: return s
        
        numCol = math.ceil(len(s) / (2*numRows - 3))
        for i in range(numRows):
            for j in range(numCol):
                inx = i + j * (numRows - 1 + numRows - 2 + 1)
                if inx >= 0 and inx < len(s): res += s[inx]
                    
                if i != 0 and i != numRows - 1:
                    diag = inx + 2*numRows - 2 - 2*i
                    if diag >=0 and diag < len(s): res += s[diag]
                        
        return res