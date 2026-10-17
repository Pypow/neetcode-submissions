class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        posDia = set() # (r + c)
        negDia = set() # (r - c)

        board = [['.'] * n for i in range(n)]

        def dfs(r):
            if r == n:
                copy = []
                for row in board:
                    copy.append("".join(row))
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r+c) in posDia or (r-c) in negDia:
                    continue
                cols.add(c)
                posDia.add(r+c)
                negDia.add(r-c)
                board[r][c] = 'Q'
                
                dfs(r+1)

                cols.remove(c)
                posDia.remove(r+c)
                negDia.remove(r-c)
                board[r][c] = '.'
        dfs(0)
        return res

