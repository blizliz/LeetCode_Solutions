class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for inx, num in enumerate(A):
            if num > A[inx + 1]:
                return inx
        