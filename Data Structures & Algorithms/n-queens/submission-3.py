class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        neg = set()     # (r-c) = k
        pos = set()     # (r+c) = k
        res = []
        sub = [['.'] * n for i in range(n)]

        def dfs(r):
            if r == n:
                copy = []
                for row in sub:
                    copy.append("".join(row))
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in pos or (r-c) in neg:
                    continue
                col.add(c)
                pos.add(r+c)
                neg.add(r-c)
                sub[r][c] = "Q"

                dfs(r + 1)

                col.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
                sub[r][c] = "."
        dfs(0)
        return res
                