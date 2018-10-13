class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {

        if(matrix.empty()) {
            return 0;
        }
        
        vector<vector<int>> maxLen(matrix.size(), vector<int>(matrix[0].size()));
        
        int ans = 0;
        
        for (int i = 0; i < matrix.size(); ++i) {
            for (int j = 0; j < matrix[0].size(); ++j) {
                ans = max(ans, LongestPath(matrix, i, j, maxLen));
            }
        }
            
        return ans;
    }
    
    int LongestPath(vector<vector<int>>& matrix, int i, int j, vector<vector<int>> &maxLen) {
        if(maxLen[i][j] > 0) {
            return maxLen[i][j];
        }
        int maxDepth = 0;
        if (i - 1 >= 0 && i - 1 < matrix.size()
           && j >= 0 && j < matrix[0].size()
           && matrix[i][j] > matrix[i - 1][j]) {
            maxDepth = max(maxDepth, LongestPath(matrix, i - 1, j, maxLen));
        }
        if (i + 1 >= 0 && i + 1 < matrix.size()
           && j >= 0 && j < matrix[0].size()
           && matrix[i][j] > matrix[i + 1][j]) {
            maxDepth = max(maxDepth, LongestPath(matrix, i + 1, j, maxLen));
        }
        if (i >= 0 && i < matrix.size()
           && j - 1 >= 0 && j - 1 < matrix[0].size()
           && matrix[i][j] > matrix[i][j - 1]) {
            maxDepth = max(maxDepth, LongestPath(matrix, i, j - 1, maxLen));
        }
        if (i >= 0 && i < matrix.size()
           && j + 1 >= 0 && j + 1 < matrix[0].size()
           && matrix[i][j] > matrix[i][j + 1]) {
            maxDepth = max(maxDepth, LongestPath(matrix, i, j + 1, maxLen));
        }
        
        maxLen[i][j] = maxDepth + 1;
        return maxLen[i][j];
    }
};