class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit = set()
        ROW, COL = len(grid), len(grid[0])
        q = deque()

        def addRoom(r, c):
            if (r < 0 or r == ROW or c < 0 or c == COL or
                grid[r][c] == -1 or (r, c) in visit):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        
        # BFS
        depth = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = depth
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
            depth += 1
        




        
            