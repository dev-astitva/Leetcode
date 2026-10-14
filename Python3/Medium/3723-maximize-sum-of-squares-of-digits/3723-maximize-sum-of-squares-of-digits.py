class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if (9*num)<sum:
            return ""

        temp=9
        res=[]
        while sum!=0:
            div=sum//temp
            if div==0:
                temp-=1
                continue
            res+=[temp]*div
            mod=sum%temp
            sum=mod
        
        r=len(res)
        res+=[0]*(num-r)
        
        return ''.join(map(str,res))