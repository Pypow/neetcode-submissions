class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        visit = set()
        for i in range(numCourses):
            adjList[i] = []
        for crs, preq in prerequisites:
            adjList[crs].append(preq)
        
        #cycle detection
        def dfs(crs):
            if crs in visit:
                return False
            if adjList[crs] == []:
                return True
            visit.add(crs)
            for preq in adjList[crs]:
                if not dfs(preq):
                    return False
            adjList[crs] = []
            visit.remove(crs)
            return True
        for crs in adjList.keys():
            if not dfs(crs):
                return False
        return True
    
        