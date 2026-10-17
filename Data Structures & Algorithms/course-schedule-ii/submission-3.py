class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cycle, visit = set(), set()
        res = []
        preMap = {crs:[] for crs in range(numCourses)}

        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visit:
                return True

            cycle.add(crs)
            for nei in preMap[crs]:
                if not dfs(nei):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        
        for crs, preq in prerequisites:
            preMap[crs].append(preq)
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
        
        