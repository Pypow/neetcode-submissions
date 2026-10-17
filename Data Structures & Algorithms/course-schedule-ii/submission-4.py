class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        for crs, preq in prerequisites:
            adj[crs].append(preq)

        visit = set()
        cycle = set()
        res = []

        def dfs(crs):
            if crs in visit:
                return True
            if crs in cycle:
                return False
            cycle.add(crs)
            for preq in adj[crs]:
                if not dfs(preq):
                    return False
            cycle.remove(crs)
            res.append(crs)
            visit.add(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res

