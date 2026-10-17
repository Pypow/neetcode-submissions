class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []

        # dfs call
        def dfs(r, c, prevh, visit):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visit or
                heights[r][c] < prevh       #imp
            ):
                return 
            visit.add((r, c))               #imp
            dfs(r + 1, c, heights[r][c], visit)
            dfs(r - 1, c, heights[r][c], visit)
            dfs(r, c + 1, heights[r][c], visit)
            dfs(r, c - 1, heights[r][c], visit)
        
        # horizontal top and last
        for c in range(cols):
            dfs(0, c, heights[0][c], pac)   
            dfs(rows-1, c, heights[rows-1][c], atl)
        
        # vertical first and last
        for r in range(rows):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, cols-1, heights[r][cols-1], atl)

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
                

        