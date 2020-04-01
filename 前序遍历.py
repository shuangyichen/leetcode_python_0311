class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        if root:
            res.append(root.val)
            res+=self.preorderTraversal(root.left)
            res+=self.preorderTraversal(root.right) 

        return res