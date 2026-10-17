class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        
        # build adj list
        for crs, preq in prerequisites:
            adj[crs].append(preq)
        
        visit = set()
        # dfs to check for cycles
        def dfs(crs):
            if crs in visit:
                return False
            if adj[crs] == []:
                return True
            visit.add(crs)
            for preq in adj[crs]:
                if not dfs(preq):      # loop detection
                    return False
            adj[crs] = []
            visit.remove(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): # graph may not be fully connected | nowhere cycle should be present
                return False
        return True
        