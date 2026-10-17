class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}     # (r, c): no of ways to reach goal
        ROWS, COLS = m, n
        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]
            if r >= ROWS or c >= COLS:
                return 0
            if r == ROWS-1 or c == COLS-1:
                return 1
            dp[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)  # down, right
            return dp[(r, c)]
        return dfs(0, 0)