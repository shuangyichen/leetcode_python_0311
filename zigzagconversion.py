class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        pernum = 2*numRows-2
        nums = int(len(s)/pernum) #zu
        new = ''
        for j in range(numRows):
            for i in range(nums):
                if j==0:
                    new+=s[i*pernum]
                elif j ==numRows-1:
                    new+=s[numRows-1+i*pernum]
                else:
                    new+=s[j+i*pernum]
                    new+=s[pernum-j+i*pernum]
            if j == 0:
                if nums*pernum<len(s):
                    new+=s[nums*pernum]
            elif j == numRows-1:
                if nums*pernum+numRows-1<len(s):
                    new+=s[nums*pernum+numRows-1]
            else:
                if j+nums*pernum<len(s):
                    new+=s[j+nums*pernum]
                if pernum-j+nums*pernum<len(s):
                    new+=s[pernum-j+nums*pernum]
        return new