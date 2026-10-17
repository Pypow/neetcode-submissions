class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # key things to note:
        # we can swim inf dist at any given t, provided elevation is LT or EQ to t
        # return the max height (or max time) along the path

        # Modified Dijkstra's Algo      |       T: O(n^2 log(n))
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        dest = (ROWS - 1, COLS - 1)
        minH = [(grid[0][0], 0, 0)]

        def addNode(w, r, c):
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or 
                (r, c) in visit):
                return
            w2 = max(w, grid[r][c])     # w is prevCost
            heapq.heappush(minH, (w2, r, c))
            visit.add((r, c))


        while minH:
            w, r, c = heapq.heappop(minH)
            if (r, c) == dest:
                return w
            visit.add((r, c))
            addNode(w, r + 1, c)
            addNode(w, r - 1, c)
            addNode(w, r, c + 1)
            addNode(w, r, c - 1)
        
            