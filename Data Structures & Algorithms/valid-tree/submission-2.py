class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        adj = defaultdict(list)

        def dfs(node, prev):
            if node in visit: 
                return False
            
            visit.add((node))
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
    
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        return dfs(0, -1) and n == len(visit)


