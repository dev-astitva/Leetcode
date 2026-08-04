class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n=len(matrix),len(matrix[0])
        t,b,l,r=0,m-1,0,n-1
        res=[]
        while l<=r and t<=b:

            for j in range(l,r+1):
                res+=[matrix[t][j]]
            t+=1

            for i in range(t,b+1):
                res+=[matrix[i][r]]
            r-=1

            if t<=b:
                for k in range(r,l-1,-1):
                    res+=[matrix[b][k]]
                b-=1
            
            if l<=r:
                for h in range(b,t-1,-1):
                    res+=[matrix[h][l]]
                l+=1

        return res 