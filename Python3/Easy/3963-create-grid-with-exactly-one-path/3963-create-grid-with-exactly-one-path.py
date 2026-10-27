class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid=[["#" for _ in range(n)] for _ in range(m)]
        grid[-1]=["." for _ in range(n)]
        for i in range(m):
            grid[i][0]="."
        return [''.join(x) for x in grid]