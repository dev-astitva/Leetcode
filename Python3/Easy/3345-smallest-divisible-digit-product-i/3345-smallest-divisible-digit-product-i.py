class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digProd(x):
            i=map(int,list(str(x)))
            r=1
            for k in i:
                if r==0:
                    break
                r*=k
            return r
            
        while True:
            if digProd(n)%t==0:
                return n
            n+=1
        