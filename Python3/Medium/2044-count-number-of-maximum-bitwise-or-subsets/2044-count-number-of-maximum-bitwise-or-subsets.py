class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def backtrack(nums,idx,currentOR,maxOR,count):
            if currentOR==maxOR:
                count[0]+=1
            
            for i in range(idx,len(nums)):
                backtrack(nums,i+1,currentOR|nums[i],maxOR,count)

        maxOR=0

        for num in nums:
            maxOR|=num
        count=[0]

        backtrack(nums,0,0,maxOR,count)

        return count[0]