class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        answer=[]
        minSeenTillNow=cost[0]

        for c in cost:
            if c<minSeenTillNow:
                minSeenTillNow=c
            answer+=[minSeenTillNow]
        
        return answer