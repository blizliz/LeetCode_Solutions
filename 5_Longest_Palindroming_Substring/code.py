class Solution:
    def expland(self, s, l, r) :
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            
        return r - l - 1
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == None: return ""
        
        start = end = 0
        for i in range(len(s)):
            len1 = self.expland(s, i, i)
            len2 = self.expland(s, i, i + 1)
            lenmax = max(len1, len2)
            if lenmax > end - start + 1:
                start = i - (lenmax - 1) // 2
                end = i + lenmax // 2
        return s[start : end+1]
        