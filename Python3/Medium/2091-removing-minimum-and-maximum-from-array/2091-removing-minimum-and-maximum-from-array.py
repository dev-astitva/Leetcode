class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 1
            
        elMinIdx=0
        elMaxIdx=0
        for i in range(n):
            el1,el2=nums[elMinIdx],nums[elMaxIdx]
            elem=nums[i]
            if elem<el1:
                elMinIdx=i
            if elem>el2:
                elMaxIdx=i

        leftIdx=min(elMinIdx,elMaxIdx)
        rightIdx=max(elMinIdx,elMaxIdx)

        bothFromLeft=rightIdx+1
        bothFromRight=n-leftIdx
        oneFromEachSide=(leftIdx+1)+(n-rightIdx)

        return min(bothFromLeft,bothFromRight,oneFromEachSide)