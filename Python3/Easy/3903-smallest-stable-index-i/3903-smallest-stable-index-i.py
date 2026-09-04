class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        pref_max=[0]*n
        pref_max[0]=nums[0]
        for i in range(1,n):
            pref_max[i]=max(pref_max[i-1],nums[i])
        
        suff_min=[0]*n
        suff_min[-1]=nums[-1]
        for j in range(n-2,-1,-1):
            suff_min[j]=min(suff_min[j+1],nums[j])
        
        for x in range(n):
            score=pref_max[x]-suff_min[x]
            if score<=k:
                return x
        
        return -1