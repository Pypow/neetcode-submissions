class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Conditions to check: 
        1. No Cycles
        2. All nodes are connected (no floating nodes)
        """
        visit, cycle = set(), set()
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(node, prev):
            if node in cycle:
                return False
            if node in visit:
                return True
            cycle.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            cycle.remove(node)
            visit.add(node)
            return True
        
        dfs(0, -1)
        return len(visit) == n
            