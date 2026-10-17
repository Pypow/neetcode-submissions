class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        res = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        minH = [[grid[0][0], 0, 0]]      # [level, r, c]
        
        while minH:
            l, r, c = heapq.heappop(minH)
            if r == N-1 and c == N-1:
                return l
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if ( nr < 0 or nc < 0 or
                    nr == len(grid) or nc == len(grid) or
                    (nr, nc) in visit 
                ):
                    continue
                visit.add((nr, nc))
                heapq.heappush(minH, [max(l, grid[nr][nc]), nr, nc])
        return res