class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minHeap = [[grid[0][0], 0, 0]]   # [cost, r, c]
        def addNei(prevCost, r, c):
            if (
                r < 0 or r == N or
                c < 0 or c == N or
                (r, c) in visit 
            ):
                return
            heapq.heappush(minHeap,[max(prevCost, grid[r][c]), r, c])

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == N - 1 and c == N - 1:
                return t
            visit.add((r, c))
            addNei(t, r + 1, c)
            addNei(t, r - 1, c)
            addNei(t, r, c + 1)
            addNei(t, r, c - 1)

            