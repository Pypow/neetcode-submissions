class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [([0] * n) for i in range(m)]

        for r in range(m):
            grid[r][n-1] = 1
        
        for c in range(n):
            grid[m-1][c] = 1
        
        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                grid[r][c] = grid[r + 1][c] + grid[r][c + 1]
        return grid[0][0]

