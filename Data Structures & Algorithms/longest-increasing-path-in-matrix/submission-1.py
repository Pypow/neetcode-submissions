class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        res = 0
        rows, cols = len(matrix), len(matrix[0])
        def dfs(r, c, prev):               
            if r < 0 or c < 0 or r >= rows or c >= cols or matrix[r][c] <= prev:
                return 0

            if (r, c) in dp:
                return dp[(r, c)]
            
            count = 1 
            count = max(count, 1 + dfs(r + 1, c, matrix[r][c]))
            count = max(count, 1 + dfs(r - 1, c, matrix[r][c]))
            count = max(count, 1 + dfs(r, c + 1, matrix[r][c]))
            count = max(count, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = count
            return dp[(r, c)]
        
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c, -1))
        return res
