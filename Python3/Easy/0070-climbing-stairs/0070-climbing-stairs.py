class Solution:
    def climbStairs(self, n: int) -> int:
        # res=1
        # def fac(x):
        #     r=1
        #     for k in range(1,x+1):
        #         r*=k
        #     return r
        # def com(n,r):
        #     return fac(n)//(fac(n-r)*fac(r))
        # temp=1
        # for a in range(n//2):
        #     res+=com(n-temp,temp)
        #     temp+=1
        # return res
        if n<3:
            return n
            
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        dp[2]=2

        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        
        return dp[n]
