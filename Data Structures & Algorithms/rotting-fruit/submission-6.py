class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        visit = set()
        time = 0
        fresh = 0
        rows, cols = len(grid), len(grid[0])

        def addNei(r, c):
            nonlocal fresh
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visit or
                grid[r][c] != 1
            ):
                return
            fresh -= 1
            grid[r][c] = 2
            q.append((r, c))
            visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                addNei(r + 1, c)
                addNei(r - 1, c)
                addNei(r, c + 1)
                addNei(r, c - 1)
            time += 1
        return time if fresh == 0 else -1