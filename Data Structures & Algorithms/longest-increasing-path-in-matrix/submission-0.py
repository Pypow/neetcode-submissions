class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        visit = {}  # (r, c): pathLen
        res = 0
        rows, cols = len(matrix), len(matrix[0])
        def dfs(r, c):
            if (r, c) in visit: 
                return visit[(r, c)]
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            length = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nc >= 0 and nr < rows and nc < cols and matrix[nr][nc] > matrix[r][c] :
                    length = max(length, 1 + dfs(nr, nc))
                
            visit[(r, c)] = length
            return visit[(r, c)]        # length
        
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))
        return res