class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        ndia = set() # r-c = k
        pdia = set() # r+c = k

        res = []
        sub = [["."] * n for i in range(n)]

        def dfs(r):
            if r == n:
                copy = []
                for tmp in sub:
                    copy.append("".join(tmp))
                res.append(copy)
                return

            for c in range(n):
                if (
                    c in cols or
                    (r - c) in ndia or
                    (r + c) in pdia
                ):
                    continue
                cols.add(c)
                ndia.add(r - c)
                pdia.add(r + c)
                sub[r][c] = "Q"

                dfs(r + 1)

                cols.remove(c)
                ndia.remove(r - c)
                pdia.remove(r + c)
                sub[r][c] = "."
        dfs(0)
        return res
