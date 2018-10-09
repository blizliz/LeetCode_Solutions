class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows == 0: return res
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1, 1]]
        
        res.extend([[1], [1, 1]])
        
        i = numRows - 2
        
        while i > 0:
            newRow = [1]
            for j in range(0, len(res[-1]) - 1):
                currRow = res[-1]
                newRow.append(currRow[j] + currRow[j + 1])
            newRow.append(1)
            res.append(newRow)
                
            i -= 1
            
        return res