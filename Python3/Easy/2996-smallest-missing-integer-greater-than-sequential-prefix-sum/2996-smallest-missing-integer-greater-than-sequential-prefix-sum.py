class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        k=set(nums)
        
        prev=[nums[0]]
        seqPref=0
        for num in nums[1:]:
            if prev[-1]+1==num:
                prev+=[num]
            else:
                break
        seqPref=max(seqPref,sum(prev))
        
        i=seqPref
        while True:
            if i not in k:
                return i
            i+=1

