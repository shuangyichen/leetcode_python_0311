class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        k = x
        now =False
        while k>0:
            mid  = int(k/2)
            if mid**2 == x: return mid
            elif mid**2>x:
                last = now
                now = False
            elif mid**2<x:
                last = now
                now = True
            if last==False and now==True:
                res = self.search(ma=k,mi=int(k/2),x=x)
                return res
            k = int(k/2)

    def search(self,ma,mi,x):
        while mi<=ma:
            mid = int((ma+mi)/2)
            if mid**2 == x: return mid
            elif mid**2>x:ma=mid-1
            elif mid**2<x:mi=mid+1
        return mi-1