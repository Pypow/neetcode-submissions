class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        visit = set()
        res = 0

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(a, prev):
            if a in visit:
                return False
            
            visit.add(a)
            for b in adj[a]:
                if b == prev:
                    continue
                dfs(b, a)
            
            return True
        for a in range(n):
            if dfs(a, -1):
                res += 1
        return res

            