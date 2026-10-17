class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}     # (r, c): max path
        def dfs(r, c, prev):
            if (r < 0 or r == rows or
                c < 0 or c == cols or
                matrix[r][c] <= prev):
                return 0
            if (r, c) in dp:            # keep it below not above guard check
                return dp[(r, c)]

            res = 1 + max(
            dfs(r + 1, c, matrix[r][c]),
            dfs(r, c + 1, matrix[r][c]),
            dfs(r - 1, c, matrix[r][c]),
            dfs(r, c - 1, matrix[r][c])
            )
            dp[(r, c)] = res
            return res
        result = 0 
        for r in range(rows):
            for c in range(cols):
                result = max(result, dfs(r, c, -1))
        return result