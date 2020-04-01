class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        if root==None:
            return res
        
        def helper(root,level):
            if len(res)<level:
                res.append([])
            res[level-1].append(root.val)
            if root.left:
                helper(root.left,level+1)   
            if root.right:
                helper(root.right,level+1)  

        helper(root,1)
        return res