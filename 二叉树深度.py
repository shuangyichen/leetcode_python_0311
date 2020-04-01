class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        return self.find(root,1)
        

    def find(self,root,depth):
        depthl=depthr=depth
        if root.left:
            depthl=1+depth
            depthl = self.find(root.left,depthl)
        if root.right:
            depthr=1+depth
            depthr = self.find(root.right,depthr)
        
        return max(depthl,depthr)