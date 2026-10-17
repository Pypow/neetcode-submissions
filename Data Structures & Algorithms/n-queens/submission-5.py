class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        pos = set()
        neg = set()
        cols = set()
        board = [["."] * n for i in range(n)]

        def dfs(r):
            if (r == n):
                sub = []
                for r in range(len(board)):
                    row = "".join(board[r])
                    sub.append(row)
                res.append(sub)
                return 

            for c in range(n):
                if (
                (r+c) in pos or
                (r-c) in neg or
                c in cols
                ):
                    continue

                board[r][c] = "Q"
                pos.add(r + c)
                neg.add(r - c)
                cols.add(c)

                dfs(r + 1)
                
                board[r][c] = "."
                pos.remove(r + c)
                neg.remove(r - c)
                cols.remove(c)

        dfs(0)
        return res