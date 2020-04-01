class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        res = []
        if n < 1:
            return res
        else:
            return self.generateBST(1, n)
        
    def generateBST(self, start, end):
        res=[]
        if start>end:
            
            return [None]
        
        for i in range(start,end+1):
            lefttree = self.generateBST(start,i-1)
            righttree = self.generateBST(i+1,end)
            for left in lefttree:
                for right in righttree:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)

        return res