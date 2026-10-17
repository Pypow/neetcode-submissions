class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        visit = set()
        

        def dfs(node):
            if adj[node] == []:
                return True
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            visit.remove(node)
            adj[node] = []
            return True

        
        for n in range(numCourses):
            adj[n] = []
        
        for n1, n2 in prerequisites:
            adj[n1].append(n2)
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True
