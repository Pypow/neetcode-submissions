class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visit = set()
        pac = set()
        atl = set()
        res = []
        
        def dfs(r, c, prev, visit):
            if (
                (r < 0 or r >= len(heights)) or
                c < 0 or c >= len(heights[0]) or
                (r, c) in visit or
                heights[r][c] < prev
            ):  
                return
            visit.add((r, c))
            dfs(r + 1, c, heights[r][c], visit)
            dfs(r - 1, c, heights[r][c], visit)
            dfs(r, c + 1, heights[r][c], visit)
            dfs(r, c - 1, heights[r][c], visit)

        for r in range(len(heights)):
            dfs(r, 0, -1, pac)
            dfs(r, len(heights[0]) - 1, -1, atl)
        
        for c in range(len(heights[0])):
            dfs(0, c, -1, pac)
            dfs(len(heights) - 1, c, -1, atl)

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res