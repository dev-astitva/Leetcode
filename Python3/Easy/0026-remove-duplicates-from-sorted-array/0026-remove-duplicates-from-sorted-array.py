class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # res=sorted(list(set(nums)))
        # k=len(res)
        # for i in range(k):
        #     nums[i]=res[i]
        # return k

        n=len(nums)
        if n==1:
            return 1
        i=0
        j=1
        k=1

        while j<n:
            check=nums[i]==nums[j]
            if check:
                j+=1
                continue
            k+=1
            i+=1
            nums[i]=nums[j]
            j+=1
        
        return k