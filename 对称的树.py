class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None:
            return True

        inorder = self.levelOrder(root)
        print(inorder)
        for i in range(1,len(inorder)):
            if len(inorder[i])%2==0:
                a = inorder[i][0:int(len(inorder[i])/2)]
                print(a)
                a.reverse()

                if a != inorder[i][(int(len(inorder[i])/2)):len(inorder[i])]:
                    return False
            else:
                return False
        return True

    def levelOrder(self, root):
        res=[]
        if root==None:
            return res
        
        def helper(root,level):
            if len(res)<level:
                res.append([])
            res[level-1].append(root.val)
            if root.left:
                helper(root.left,level+1)   
            elif root.left==None:
                if len(res)<level+1:
                    res.append([])
                res[level].append('none')
            if root.right:
                helper(root.right,level+1)  
            elif root.right==None:
                if len(res)<level+1:
                    res.append([])
                res[level].append('none')

        helper(root,1)
        return res