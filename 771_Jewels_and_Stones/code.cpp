class Solution {
public:
    int numJewelsInStones(string J, string S) {
        set<int> jewels;
        for (int i = 0; i < J.size(); ++i) {
            jewels.insert(J[i]);
        }
        
        int ans = 0;
        
        for(int i = 0; i < S.size(); ++i) {
            if (jewels.find(S[i]) != jewels.end()) ++ans;
        }
        
        return ans;
    }
};