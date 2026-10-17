class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS solution
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visit = set()

        # helper
        def addNode(r, c):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visit or
                grid[r][c] == -1
            ):
                return
            q.append((r, c))
            visit.add((r, c))


        # add all treasuer chests to q
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        # bfs from all treasures
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist       
                addNode(r + 1, c)
                addNode(r - 1, c)
                addNode(r, c + 1)
                addNode(r, c - 1)
            dist += 1
        
