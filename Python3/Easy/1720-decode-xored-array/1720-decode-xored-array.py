class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        #main target=encoded[0] from these arr[0]=first and arr[1] to find
        arrEl1=0
        while True:
            if first^arrEl1==encoded[0]:
                break
            arrEl1+=1
        res=[first,arrEl1]
        for i in range(1,len(encoded)):
            res+=[res[i]^encoded[i]]
        return res