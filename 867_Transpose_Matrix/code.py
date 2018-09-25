class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        
        for i in range(len(A[0])):
            res.append([row[i] for row in A])
                
        return res