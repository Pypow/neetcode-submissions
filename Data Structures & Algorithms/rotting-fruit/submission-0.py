class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        def addRotten(r, c):
            nonlocal fresh
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or (r,c) in visit:
                return
            visit.add((r, c))
            grid[r][c] = 2
            fresh -= 1
            q.append((r, c))
                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    visit.add((r, c))
                    q.append((r, c)) 
        
        time = 0
        while q and fresh:
            for i in range(len(q)):
                r, c = q.popleft()
                addRotten(r+1, c)
                addRotten(r-1, c)
                addRotten(r, c+1)
                addRotten(r, c-1)

            time += 1
        
        return time if fresh == 0 else -1