class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Prim's Algo:
        A greedy method for building a minimum spanning tree
        by starting at any vertex and repeatedly adding 
        the smallest edge that connects the growing tree 
        to a new vertex.
        """
        # in this prob, need to build edges and hence adj list  
        N = len(points) 
        adj = {i: [] for i in range(N)}     # we will treat each point as idx
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):       # i+1 because, we don't want to connect same point
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([cost, j])
                adj[j].append([cost, i])    # undirected edge, conected means in both ways
        
        res = 0
        visit = set() # idx
        minH = [[0, 0]]   # [cost, idx]
        # prim's
        while len(visit) < N:   # all points are visited/ connected
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            visit.add(i)
            res += cost
            for neiCost, neiIdx in adj[i]:
                if neiIdx not in visit:
                    heapq.heappush(minH, [neiCost, neiIdx])
        return res




