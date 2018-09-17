class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = ans = 0
        map = {}
        
        for j, ch in enumerate(s):
            if ch in map:
                i = max(i, map[ch])
            ans = max(ans, j - i + 1)
            map[ch] = j + 1
            
        return ans