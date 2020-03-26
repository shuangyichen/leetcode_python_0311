class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
           return 1
        k = abs(n)
        half = self.myPow(x,int(k/2))
        if n%2!=0:
            res = half*half*x
        elif n%2==0:
            res = half*half


        if n>0:
            return res
        elif n<0:
            return 1/res