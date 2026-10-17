class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()
        time = 0
        fresh = [0]
        def addNode(r, c):
            if (
                r not in range(rows) or
                c not in range(cols) or
                (r, c) in visit or
                grid[r][c] != 1
            ):
                return
            
            visit.add((r, c))
            grid[r][c] = 2
            q.append((r, c))
            fresh[0] -= 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh[0] += 1
                if grid[r][c] == 2:
                    visit.add((r, c))
                    q.append((r, c))

        time = 0
        while q and fresh[0]:
            for i in range(len(q)):
                r, c = q.popleft()
                addNode(r+1, c)
                addNode(r-1, c)
                addNode(r, c+1)
                addNode(r, c-1)
            time += 1
            
        return time if fresh[0] == 0 else -1


