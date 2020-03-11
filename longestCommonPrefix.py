class Solution:
    def longestCommonPrefix(self, List) -> str:
        if len(List) == 0:
            return ''
        if len(List) == 1:
            return List[0]
        maxindex = 0
        myList = sorted(List,key = lambda i:len(i),reverse=False)
        minlen = len(myList[0])
        for i in range(minlen):
            for j in range(len(List)-1):
                if List[j][i]==List[j+1][i]:
                    if j ==len(List)-2:
                        if maxindex<=i:
                            maxindex = i+1
                else:
                    return List[0][0:maxindex]
        return List[0][0:maxindex] 

#利用python比较字符串的功能，越前面的越大则整体越大
class Solution:
    def longestCommonPrefix(self, List) -> str:
        if len(List)==0:
            return ''
        maxkey = max(List)
        minkey = min(List)
        index = 0
        for i in range(min(len(maxkey),len(minkey))):
            if minkey[i] == maxkey[i]:
                index = i+1
            else:
                return minkey[0:index]
        return minkey[0:index]

#zip折叠，set 去重
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = zip(*strs)
        lists = list(a)
        res = ''
        for i in range(len(lists)):
            q = tuple(set(lists[i]))            
            if len(q)!=1:
                return res
            res = res+q[0]
        return res
            
        