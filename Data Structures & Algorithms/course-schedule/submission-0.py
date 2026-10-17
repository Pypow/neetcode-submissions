class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {crs:[] for crs in range(numCourses)}
        visit = set()

        # Add prerequisite to each node
        for crs, preq in prerequisites:
            preMap[crs].append(preq)

        def dfs(crs):
            if preMap[crs] == []:
                return True
            if crs in visit:
                return False

            visit.add(crs)
            for preq in preMap[crs]:
                if not dfs(preq):
                    return False
            visit.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

