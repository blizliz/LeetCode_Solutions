class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        map = {}
        self.makeMap(root, map, k)
        if len(map) < 2:
            return False
        
        for key in map:
            if map[key] in map: 
                if key != map[key]:
                    return True
        return False
        
    def makeMap(self, root, map, k):
        if not root:
            return 
        else:
            map[root.val] = k - root.val
            self.makeMap(root.left, map, k)
            self.makeMap(root.right, map, k)