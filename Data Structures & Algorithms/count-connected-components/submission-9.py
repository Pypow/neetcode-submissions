class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par  = [i for i in range(n)]    # stores parents (root parents)
        rank = [1] * n                  # stores height of each tree

        def find(node):
            res = node
            while res != par[res]:
                par[res] = par[par[res]]        # path compression
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:                        # cycle detection 
                return 0

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res
