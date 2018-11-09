class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1: return [0]
        
        degrees = [0] * n
        graph = {x: [] for x in range(n)}
        
        for edge in edges:
            degrees[edge[0]] += 1
            degrees[edge[1]] += 1
            
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        ends = [x for x in range(n) if degrees[x] == 1]
        
        roots = []
        while ends:
            temp = []
            roots = ends
            for end in ends:
                for n in graph[end]:
                    degrees[n] -= 1
                    if degrees[n] == 1: temp.append(n)
            ends = temp
            
                
        return roots
    