class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        visit = set()

        for crs, preq in prerequisites:
            adj[crs].append(preq)

        def dfs(crs):
            if crs in visit:
                return False
            
            if len(adj[crs]) == 0:
                return True
            
            visit.add(crs)
            for preq in adj[crs]:
                if not dfs(preq):
                    return False
            adj[crs] = []
            visit.remove(crs)
            return True
        
        for crs in adj:
            if not dfs(crs):
                return False
        return True