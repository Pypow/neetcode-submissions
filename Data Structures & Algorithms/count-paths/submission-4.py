class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n
        dp = {}     # (r, c): no of paths to target
        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]
            if r > rows or c > cols:
                return 0
            if r == m-1 and c == n-1:
                return 1
            paths = 0
            paths += dfs(r + 1, c)  # down
            paths += dfs(r, c + 1)  # right
            dp[(r, c)] = paths
            return paths
        
        return dfs(0, 0)

