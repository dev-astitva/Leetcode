class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        strictly_inc=[]
        for i in range(n):
            for j in range(i+1,n+1):
                temp=nums[i:j]
                if len(set(temp))==len(temp):
                    if sorted(temp)==temp:
                        strictly_inc.append(len(temp))
        strictly_dec=[]
        for a in range(n):
            for b in range(a+1,n+1):
                temp=nums[a:b]
                if len(set(temp))==len(temp):
                    if sorted(temp)[::-1]==temp:
                        strictly_dec.append(len(temp))
        s_i=max(strictly_inc) if len(strictly_inc)!=0 else 0
        s_d=max(strictly_dec) if len(strictly_dec)!=0 else 0
        return max(s_i,s_d)