class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        res = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r not in range(rows) or
                c not in range(cols) or
                (r, c) in visit or
                grid[r][c] == 0
            ):
                return 0
            
            visit.add((r, c))
            count = 1

            # recursive search in neighbors
            count += dfs(r+1, c) 
            count += dfs(r-1, c) 
            count += dfs(r, c+1) 
            count += dfs(r, c-1) 
            return count
        
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))
        return res
