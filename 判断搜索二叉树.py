#无法验证二叉搜索树的爷孙关系
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root==None:
            return True
        if root:
            if root.left:
                if root.left.val>=root.val:
                    return False
                if self.isValid(root.left,min1)==False:
                    return False
                
            if root.right:
                if root.val>=root.right.val:
                    return False
                if self.isValid(root.right,maxr)==False:
                    return False
            return True
#先中序遍历再删去重复的
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        inorder = self.inorderTraversal(root)
        
        if inorder == list(sorted(set(inorder))):
            return True
        else:
            return False

    def inorderTraversal(self, root: TreeNode):
        res=[]
        if root:
            res+=self.inorderTraversal(root.left)
            res.append(root.val)
            res+=self.inorderTraversal(root.right) 
        return res