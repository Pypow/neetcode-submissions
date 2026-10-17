class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visit = set()
        cycle = set()
        preMap = {crs:[] for crs in range(numCourses)}

        for crs, preq in prerequisites:
            preMap[crs].append(preq)
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for p in preMap[crs]:
                if not dfs(p):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res 
            
