class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[]
        for num in range(nums[0],nums[-1]+1):
            if num not in nums:
                res+=[num]
        return res
        