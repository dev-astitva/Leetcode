class Solution:
    def trailingZeroes(self, n: int) -> int:
        res=0
        k=1
        while True:
            temp=n//(5**k)
            if temp==0:
                return res
            else:
                res+=temp
                k+=1