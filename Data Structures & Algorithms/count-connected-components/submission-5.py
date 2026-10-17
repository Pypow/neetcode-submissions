class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        adj = {i:[] for i in range(n)}
        count = 0

        def dfs(node, prev):
            if node in visit:
                return
            
            visit.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                dfs(nei, node)

        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        for node in range(n):
            if node not in visit:
                count += 1
            dfs(node, -1)
        return count


    
        