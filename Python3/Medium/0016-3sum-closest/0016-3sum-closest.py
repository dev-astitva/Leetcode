class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        closest_val=float('inf')
        closest_total=float('inf')
        nums.sort()
        for i in range(n):
            
            a=nums[i]
            l,r=i+1,n-1
            
            while l<r:
                b,c=nums[l],nums[r]
                total=a+b+c
                diff=abs(target-total)
                if diff<closest_val:
                    closest_val=diff
                    closest_total=total
                
                if total>target:
                    r-=1
                else:
                    l+=1
        return closest_total