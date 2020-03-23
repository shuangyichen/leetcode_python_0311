class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==0:
            return True
        a = list(s)
        a = ['(','[','{']
        b = [')',']','}']
        if len(s)%2==1:
            return False
        for i,left in enumerate(a):
            if left in s:
                numl = [index for (index,value) in enumerate(s) if value == left]
                numr = [index for (index,value) in enumerate(s) if value == b[i]]
                if len(numl)!=len(numr):
                    return False
                deltasum = sum(numl)-sum(numr)
                if len(numl)%2==1 and deltasum%2==0:
                    return False
                elif len(numl)%2==0 and deltasum%2==1:
                    return False
                    
        return True