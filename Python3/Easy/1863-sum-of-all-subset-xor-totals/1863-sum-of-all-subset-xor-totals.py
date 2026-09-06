class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def zeroPad(y,p):
            m=len(y)
            return (p-m)*"0"+y

        def func(x):
            n=len(x)
            res=0
            for i in range(1,(2**n)):
                b=zeroPad(bin(i)[2:],n)
                temp=0
                for j in range(n):
                    if b[j]=="1":
                        temp^=x[j]
                res+=temp
            return res               
        
        return func(nums)