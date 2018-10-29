class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def trans(s):
            res = []
            for ch in s:
                if ch != "#":
                    res.append(ch)
                else:
                    res = res[:-1]
            return res

        return trans(S) == trans(T)