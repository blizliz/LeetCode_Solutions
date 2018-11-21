class Solution:
    def isPalindrome(self, s, l, r):
        for i in range(l, r):
            if s[i] != s[r - i + l]:
                return False
        return True
    
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        size = len(s)
        for l in range(size // 2):
            if s[l] != s[size - 1 - l]:
                r = size - 1 - l
                return self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1)
        return True