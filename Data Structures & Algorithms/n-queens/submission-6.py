class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for i in range(n)]
        cols = set()
        pos = set()
        neg = set()

        def dfs(r):
            if r == n:
                sub = []
                for i in range(len(board)):
                    row = "".join(board[i])
                    sub.append(row)
                res.append(sub)
                return

            for c in range(n):
                if (
                    (r + c) in pos or
                    (r - c) in neg or
                    c in cols
                ):  
                    continue
                
                board[r][c] = "Q"
                pos.add((r + c))
                neg.add((r - c))
                cols.add(c)

                dfs(r + 1)

                board[r][c] = "."
                pos.remove((r + c))
                neg.remove((r - c))
                cols.remove(c)
        dfs(0)
        return res
