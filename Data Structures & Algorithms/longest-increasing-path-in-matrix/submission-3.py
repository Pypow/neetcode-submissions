class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # bruteforce - no memoization
        dp = {} # (r, c): vals
        res = 0
        rows, cols = len(matrix), len(matrix[0])
        visit = set()
        def dfs(r, c, prev):
            nonlocal res
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visit or
                prev >= matrix[r][c] 
            ):
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
                
            visit.add((r, c))
            tmp = 1
            tmp += max((
                dfs(r+1, c, matrix[r][c]), 
                dfs(r-1, c, matrix[r][c]),
                dfs(r, c+1, matrix[r][c]),
                dfs(r, c-1, matrix[r][c])
            ))
            visit.remove((r, c))
            dp[(r, c)] = tmp
            res = max(res, tmp)
            return tmp

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, -1)
        return res