class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        data={}
        for num in arr:
            if num in data:
                data[num]+=1
            else:
                data[num]=1
        
        vals=list(data.values())
        return len(vals)==len(set(vals))