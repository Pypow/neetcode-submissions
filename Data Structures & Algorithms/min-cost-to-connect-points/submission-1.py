class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i:[] for i in range(len(points))}    # i: [cost, j]
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([cost, j]) 
                adj[j].append([cost, i]) 

        minH = [[0, 0]]
        visit = set()
        cost = 0
        while minH:
            c, i = heapq.heappop(minH)
            if i in visit:
                continue
            visit.add(i)
            cost += c
        
            for ncost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [ncost, nei])
        return cost
                    
            