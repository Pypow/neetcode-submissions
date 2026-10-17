class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        res = 0
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if r >= rows or c >= cols or r < 0 or c < 0 or grid[r][c] == "0" or (r, c) in visit:
                return 
            
            visit.add((r, c))

            dfs(r+1, c) 
            dfs(r-1, c) 
            dfs(r, c+1) 
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    res += 1
                    dfs(r, c)
        return res
            