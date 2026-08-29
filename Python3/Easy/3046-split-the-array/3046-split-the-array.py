class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        data={}
        for num in nums:
            data[num]=data.get(num,0)+1
        for k,v in data.items():
            if v>2:
                return False
        return True