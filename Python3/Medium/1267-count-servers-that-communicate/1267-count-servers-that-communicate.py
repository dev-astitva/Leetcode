class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        r,c=len(grid),len(grid[0])
        mat=[]
        for i in grid:
            mat+=i
        def chkfor1inSurr(x,y):
            if y>0 and 1 in grid[x][:y]:#left
                # print(grid[x][:y],"l")
                return True
            if y<c-1 and 1 in grid[x][y+1:]:#right
                # print(grid[x][y+1:],"r")
                return True
            if x>0 and 1 in mat[y:x*c+y:c]:#top
                # print(mat[y:x*c+y:c],"t")
                return True
            if x<r-1 and 1 in mat[x*c+y::c][1:]:#bottom
                # print(mat[x*c+y::c][1:],"b")
                return True
            return False
        res=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]!=0 and chkfor1inSurr(i,j):
                    res+=1
        return res