class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i:[] for i in range(len(points))}    # i: list of [cost, j]
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        # prim's algo
        visit = set()
        res = 0
        minH = [[0, 0]]
        while len(visit) < len(points):
            cost, i = heapq.heappop(minH)
            if i in visit: 
                continue
            res += cost
            visit.add(i)
            for nCost, neig in adj[i]:
                if neig not in visit:
                    heapq.heappush(minH, [nCost, neig])
        return res