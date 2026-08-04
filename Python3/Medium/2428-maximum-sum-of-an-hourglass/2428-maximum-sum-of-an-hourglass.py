class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxVal=0
        m,n=len(grid),len(grid[0])
        def calc(x,y):
            # total=0
            # for i in range(x,x+3):
            #     for j in range(y,y+3):
            #         if i==x+1 and (j==y or j==y+2):
            #             continue
            #         total+=grid[i][j]
            
            total=grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]
            return total

        for i in range(m-2):
            for j in range(n-2):
                maxVal=max(maxVal,calc(i,j))
        
        return maxVal            