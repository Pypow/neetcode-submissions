class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        def dfs(node, target, visit):
            if node == target:
                return True
            
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    if dfs(nei, target, visit):
                        return True
            return False

        
        for n1, n2 in edges:
            visit = set()
            if n1 in adj and n2 in adj and dfs(n1, n2, visit):
                return [n1, n2]
            
            adj[n1].append(n2)
            adj[n2].append(n1)
        