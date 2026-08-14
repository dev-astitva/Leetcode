class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        seen={}
        res=2
        prev=curr=0
        n=len(s)
        for i in range(n):
            el=s[i]
            curr=i
            if el in seen:
                if seen[el]==2:
                    res=max(res,curr-prev)
                    for j in range(prev,curr-1):
                        if s[j]==el:
                            prev=j+1
                            seen[el]=2
                            break
                else:
                    seen[el]+=1
            else:
                seen[el]=1
            
            seen={}
            for j in range(prev,curr+1):
                seen[s[j]]=seen.get(s[j],0)+1

            res=max(res,curr-prev+1)
            
        
        return res
                
