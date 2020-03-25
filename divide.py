class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dividendM = abs(dividend)
        divisorM = abs(divisor)
        num = 0
        for i in range(31,-1,-1):
            if dividendM/2**i>=divisorM:
                dividendM = dividendM - divisorM*(2**i)
                num+=2**i
                if dividendM < divisorM:
                    break
                
        if (dividend>0 and divisor>0) or(dividend>0 and divisor>0):
            num = num
        elif (dividend>0 and divisor<0) or(dividend<0 and divisor>0):
            num = -num

        if num<-2**31 or num>2**31-1:
            return 2**31-1
        return num