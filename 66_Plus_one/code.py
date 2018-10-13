class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        rem = 1
        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i] + rem
            rem = digit // 10
            digit = digit % 10
            digits[i] = digit
            if rem == 0: return digits
        if rem == 1: return [1] + digits
        return digits