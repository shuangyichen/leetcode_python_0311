class Solution:
    def lengthOfLongestSubstring(self,s):
        sub = []
        start = 0
        maxlenth = 0
        if len(s)==1:
            maxlenth = 1
            return maxlenth 
        for i in range(1,len(s)):
            sub = s[start:i]

            if s[i] not in sub:
                lenth = len(sub)+1
            else:
                start = sub.index(s[i]) + 1 + start
                lenth = len(sub)
            if maxlenth < lenth:
                maxlenth = lenth

        return maxlenth