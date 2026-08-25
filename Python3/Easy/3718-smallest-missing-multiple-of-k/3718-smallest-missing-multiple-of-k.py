class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        multiples=set()
        n=len(nums)
        
        for i in range(1,n+1):
            multiples.add(k*i)

        for num in nums:
            if num in multiples:
                multiples.remove(num)
        
        if not multiples:
            return k*(n+1)
        else:
            minVal=float('inf')
            for num in multiples:
                minVal=min(minVal,num)
            return minVal
            