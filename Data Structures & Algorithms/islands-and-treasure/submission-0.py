class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit = set()
        q = deque()
        rows, cols = len(grid), len(grid[0])
        
        def addNode(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == -1 or (r, c) in visit:
                return 
            visit.add((r, c))
            q.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        
        dist = 0

        while q:
            for i in range(len(q)):     # snapshot of q
                r, c = q.popleft()
                grid[r][c] = dist

                addNode(r+1, c)
                addNode(r-1, c)
                addNode(r, c+1)
                addNode(r, c-1)
            dist += 1
        
