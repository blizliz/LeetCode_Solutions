class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& A) {
        vector<vector<int>> transA(A[0].size(), vector<int>(A.size()));
        
        for(int i = 0; i < A.size(); ++i) {
            for (int j = 0; j < A[0].size(); ++j) {
                transA[j][i] = A[i][j];
            }
        }
        
        return transA;
    }
};