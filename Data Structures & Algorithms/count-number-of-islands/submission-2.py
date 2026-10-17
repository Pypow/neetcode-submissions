class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or 
                (r, c) in visit or
                grid[r][c] == "0"
            ):
                return False

            visit.add((r, c))
            # explore neighbors
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return True
        

        res = 0

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c):
                    res += 1
        return res