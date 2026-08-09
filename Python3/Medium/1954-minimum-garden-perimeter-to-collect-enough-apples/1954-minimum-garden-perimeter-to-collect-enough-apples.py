class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        cnt=0
        total=0
        while total<neededApples:
            cnt+=1
            total+=12*cnt*cnt
        return 8*cnt