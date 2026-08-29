class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        res=0
        for i in range(len(nums)-1):
            el1,el2=nums[i],nums[i+1]
            res=max(el2-el1,res)
        return res