class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        def dfs(node, target, visit):           # does path exist?
            if node == target:
                return True
            visit.add(node)
            for neighbor in adj[node]:
                if neighbor not in visit:
                    if dfs(neighbor, target, visit):
                        return True
            return False
        
        for n1, n2 in edges:
            visit = set()
            if n1 in adj and n2 in adj and dfs(n1, n2, visit):
                return [n1, n2]
            adj[n1].append(n2)
            adj[n2].append(n1)



        

