class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digSum(x):
            return sum(map(int,list(str(x))))
        for i in range(len(nums)):
            if digSum(nums[i])==i:
                return i
        return -1