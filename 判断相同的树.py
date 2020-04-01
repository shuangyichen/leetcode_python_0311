class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p==None and q==None:
            return True
        elif p==None or q==None:
            return False
        if p:
            if q:
                if p.val==q.val:
                    if self.isSameTree(p.left,q.left)==True and self.isSameTree(p.right,q.right)==True:
                        return True
                    else:
                        return False
                else:
                    return False