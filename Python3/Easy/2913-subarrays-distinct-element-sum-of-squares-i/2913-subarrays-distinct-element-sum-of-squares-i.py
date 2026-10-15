class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        for i in range(n):
            for j in range(i,n):
                res+=(len(set(nums[i:j+1])))**2
        return res