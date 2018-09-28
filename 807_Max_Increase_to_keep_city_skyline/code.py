class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        maxRow = []
        maxCol = []
        res = 0
        
        for row in grid:
            maxRow.append(max(row))
            
        for i in range(len(grid[0])) :
            maxCol.append(max([row[i] for row in grid]))
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                m = min(maxRow[i], maxCol[j])
                res += m - grid[i][j]
                
        return res
            