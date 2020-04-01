class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        if root:
            res+=self.preorderTraversal(root.left)
            res+=self.preorderTraversal(root.right) 
            res.append(root.val)
        return res