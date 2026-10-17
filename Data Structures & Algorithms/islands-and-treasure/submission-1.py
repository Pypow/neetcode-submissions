class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit = set()
        q = deque()
        rows, cols = len(grid), len(grid[0])

        def addNode(r, c, count):
            if (
                r not in range(rows) or
                c not in range(cols) or
                (r, c) in visit or
                grid[r][c] == -1 or
                grid[r][c] == 0
            ):
                return 
            
            visit.add((r, c))
            grid[r][c] = count

            q.append((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        count = 0     
        while q:
            count += 1

            for i in range(len(q)):
                r, c = q.popleft()
                addNode(r+1, c, count)
                addNode(r-1, c, count)
                addNode(r, c+1, count)
                addNode(r, c-1, count)
        

