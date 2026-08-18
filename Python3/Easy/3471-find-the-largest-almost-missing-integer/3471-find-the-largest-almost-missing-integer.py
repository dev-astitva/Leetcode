class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        
        if k==1:
            data={}
            res=None
            for num in nums:
                data[num]=data.get(num,0)+1
            for k,v in data.items():
                if v==1:
                    if not res:
                        res=k
                    else:
                        res=max(res,k)
            return res if res else -1
        
        elif k==n:
            return max(nums)

        else:
            data={}
            a,b=nums[0],nums[-1]
            data[a]=data.get(a,0)+1
            data[b]=data.get(b,0)+1

            for i in range(1,n-1):
                el=nums[i]
                if el==a or el==b:
                    data[el]+=1
                if sorted(data.values())[0]>1:
                    return -1
                    
            if data[a]==data[b]==1:
                return max(a,b)
            else:
                if data[a]==1:
                    return a
                elif data[b]==1:
                    return b
                else:
                    return -1