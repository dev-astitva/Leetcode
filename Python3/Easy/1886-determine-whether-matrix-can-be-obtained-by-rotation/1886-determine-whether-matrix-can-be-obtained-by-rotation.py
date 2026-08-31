class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate90deg(x):
            n=len(x)
            res=[[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    el=x[i][j]
                    res[j][n-i-1]=el
            return res
        a=rotate90deg(mat)
        b=rotate90deg(a)
        c=rotate90deg(b)
        return a==target or b==target or c==target or mat==target
