class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visit or
                grid[r][c] == 0
            ):
                return 0
            visit.add((r, c))
            count = 1

            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)
            return count

        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))
        return res