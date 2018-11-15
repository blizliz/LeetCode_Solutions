class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        stack = []
        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
            else:
                if not stack: return False
                if ch == ")":
                    if stack.pop() != "(": return False
                elif ch == "}":
                    if stack.pop() != "{": return False
                elif ch == "]":
                    if stack.pop() != "[": return False
                    
        if not stack:
            return True
        else:
            return False
                