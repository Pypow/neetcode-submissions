class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Conditions to check: 
        1. No Cycles
        2. All nodes are connected (no floating nodes)
        Note: 
        cycle detection in undirected, one visit set + prev node is enough.
        """
        visit = set()
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)             # imp: keep it here
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        if not dfs(0, -1):              # imp: check return value
            return False    
        return len(visit) == n
            