class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxVal=0
        m,n=len(grid),len(grid[0])
        def calc(x,y):
            total=0
            for i in range(x,x+3):
                for j in range(y,y+3):
                    if i==x+1 and (j==y or j==y+2):
                        continue
                    total+=grid[i][j]
            return total

        for i in range(m-2):
            for j in range(n-2):
                maxVal=max(maxVal,calc(i,j))
        
        return maxVal            