import heapq
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        pq = []
        
        for key in counts:
            heapq.heappush(pq, (counts[key], key))
            
        large = heapq.nlargest(k, pq, key=None)
        res = []
        for i in large:
            res.append(i[1])
        return res