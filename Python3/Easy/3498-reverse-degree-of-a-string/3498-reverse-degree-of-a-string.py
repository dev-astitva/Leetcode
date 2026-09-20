class Solution:
    def reverseDegree(self, s: str) -> int:
        res,j=0,0
        for i in s:
            j+=1
            res+=j*(26-(ord(i)-ord('a')))
        return res