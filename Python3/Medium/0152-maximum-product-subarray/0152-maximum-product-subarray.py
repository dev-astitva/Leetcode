class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd=nums[0]
        minProd=nums[0]
        res=maxProd
        n=len(nums)

        for i in range(1,n):
            num=nums[i]
            if num<0:
                maxProd,minProd=minProd,maxProd
            
            maxProd=max(num,maxProd*num)
            minProd=min(num,minProd*num)

            res=max(res,maxProd)
        
        return res
