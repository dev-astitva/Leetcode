class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)
        negs=n//2
        nums=[abs(x) for x in nums]
        nums.sort()
        a=sum([x**2 for x in nums[negs:]])
        b=sum([x**2 for x in nums[:negs]])
        return a-b