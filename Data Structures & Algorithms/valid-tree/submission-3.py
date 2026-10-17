class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True

        visit = set()
        adj = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(n1, prev):
            # cycle?
            if n1 in visit:
                return False
            visit.add(n1)
            for n2 in adj[n1]:
                if n2 == prev:
                    continue
                if not dfs(n2, n1):
                    return False
            return True

        if not dfs(0, -1):
            return False
        return len(visit) == n