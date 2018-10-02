class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxSq = 0;
        
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                maxSq = max(maxSq, DFS(grid, i , j));
            }
        }
        
        return maxSq;
    }
    
    int DFS(vector<vector<int>>& grid, int i, int j) {
        int ans = 0;
        if (grid[i][j] == 0) {
            return 0;
        } else {
            ++ans;
            grid[i][j] = 0;
            //i j-1
            //i j+1
            //i-1 j
            //i+1 j
            if (j - 1 >= 0) {
                ans += DFS(grid, i, j - 1);
            }
            if (j + 1 < grid[0].size()) {
                ans += DFS(grid, i, j + 1);
            }
            if (i - 1 >= 0) {
                ans += DFS(grid, i - 1, j);
            }
            if (i + 1 < grid.size()) {
                ans += DFS(grid, i + 1, j);
            }
        }
        
        return ans;
    }
};