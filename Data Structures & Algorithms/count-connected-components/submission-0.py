class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(i):
            if i in visit:
                return True
            visit.add(i)
            for j in adj[i]:
                dfs(j)
            return True

        count = 0
        for i in range(n):
            if i not in visit:
                count += 1
            dfs(i)
        return count